import re
import glob
import ClauseWizard
import json
import pyradox

from utils import *
from triggers.trigger import Trigger
from country.country import Country

countryDirectory = "./history/countries"
tagFile = './common/country_tags/00_countries.txt'

uniqueIdeasFile = './common/ideas/00_country_ideas.txt'

# for group ideas
groupIdeasFile = './common/ideas/zz_group_ideas.txt'

# for generic ideas
genericIdeasFile = './common/ideas/zzz_default_idea.txt'

# for Eu4 Idea Groups
basicIdeasFile = './common/ideas/00_basic_ideas.txt'

allTriggers = './data/triggers.json'
nationalTriggerPath = 'data/nat_idea_triggers.json'
groupTriggerPath = 'data/group_idea_triggers.json'

# for idea set that differ substantially from what is displayed by EU4 UI
nameConverterDict = {
    'spy': 'espionage',
    'default': 'generic'
}

english_localisation = './localisation/countries_l_english.yml'

english_names = pyradox.yml.parse_file(english_localisation)

def country_to_tag_library():
    '''
    generate a library, matching country name to tags
    '''
    library = {}
    for key, name in english_names.items():
        # all tags are of len 3 in the localisation files, so it's easy to identify
        # pyradox turns keys to lower case, should keep them uppercase for easier reference with history
        if len(key) == 3:
            library[name.lower()] = key.upper()

    for countryPath in glob.glob(countryDirectory + '/*.txt'):
        # some tags aren't in the localisation files, so we must use the other source of truth: history files.
        country = countryPath.split("/")[-1]
        country = country.split("-")
        tag = country[0].strip()
        countryName = country[1].strip(".txt").strip()
        library[countryName.lower()] = tag
        countryName = countryName.lower()
        countryName = re.sub('empire', '', countryName)
        if tag not in library:
            library[countryName.strip()] = tag
    return library

def gen_tag_library():
    '''
    generate tag -> country library using the histories folder, creating a country tag summarizing the country's
    starting position
    '''

    tagMap = {}
    for countryPath in glob.glob(countryDirectory+'/*.txt'):
        country_tree = load_country(countryPath)
        country = countryPath.split("/")[-1]
        country = country.split("-")
        tag = country[0].strip()
        tagMap[tag] = Country(tag, country_tree)

    return tagMap

def gen_country_ideas_library():
    '''
    Generate a dict of all idea sets

    EU4 stores its idea sets in several different files as of this moment, so we need to grab each file from the
    file location and collect the ideasets
    '''
    # print(tagLib)
    ideasLib = {}
    add_ideas(uniqueIdeasFile, ideasLib)
    add_ideas(groupIdeasFile, ideasLib)
    add_ideas(genericIdeasFile, ideasLib)
    return ideasLib

def gen_non_national_ideas_library():
    '''
    Generate a library consisting only the idea sets that are not National ideas,

    This is used to set up the fuzzy search algorithm in case the query string matches one of these ideas better than
    a potential country tag.

    Since All EU4 ideas are of the string "IDEANAME_ideas", we also need to remove the "_ideas" bit at the end, to
    reduce missed hits on fuzzy search. Certain ideasets are also named differently than the display, so that also need
    to be addressed.
    '''
    nonNatIdeasLib = {}
    add_basic_ideas(groupIdeasFile, nonNatIdeasLib)
    add_basic_ideas(genericIdeasFile, nonNatIdeasLib)
    add_basic_ideas(basicIdeasFile, nonNatIdeasLib)
    return nonNatIdeasLib

def add_ideas(file, dictionary):
    '''
    add the ideasets from an idea group file into the general library.
    '''
    with open(file, 'r') as t:
        clauseIdeas = ClauseWizard.cwparse(t.read())
        ideasJson = ClauseWizard.cwformat(clauseIdeas)
        for ideaName, ideaSet in ideasJson.items():
            dictionary[ideaName] = ideaSet
    return dictionary

def add_generic_ideas(file, dictionary):
    '''
    add the ideasets from either group ideaset or generic ideaset into the ideas library.
    '''
    with open(file, 'r') as t:
        clauseIdeas = ClauseWizard.cwparse(t.read())
        ideasJson = ClauseWizard.cwformat(clauseIdeas)
        for ideaName, ideaSet in ideasJson.items():
            ideaTag = re.search('(.*)_ideas', ideaName)
            dictionary[ideaTag.group(1)] = ideaSet
    return dictionary

def add_basic_ideas(file, dictionary):
    with open(file, 'r') as t:
        clauseIdeas = ClauseWizard.cwparse(t.read())
        ideasJson = ClauseWizard.cwformat(clauseIdeas)
        for ideaName, ideaSet in ideasJson.items():
            ideaTag = re.search('(.*)_ideas', ideaName)
            # if the name needs correction, fetch it.
            if ideaTag.group(1) in nameConverterDict:
                dictionary[nameConverterDict[ideaTag.group(1)]] = ideaSet
            else:
                dictionary[ideaTag.group(1)] = ideaSet
    return dictionary

def store_triggers():
    '''
    Function for collecting and storing triggers for all idea sets in the game, and dumping it into
    their respective trigger files:
    data/nat_idea_triggers.json
    data/group_idea_triggers.json

    Note: ideasets with no triggers are represented with {}
    '''
    nat_triggers = collect_triggers(uniqueIdeasFile, {})
    group_triggers = collect_triggers(groupIdeasFile, {})

    # basic idea groups do not have triggers and are not involved in trigger calcs, so they're ignored.
    with open(nationalTriggerPath, 'w') as nat, open(groupTriggerPath, 'w') as group:
        json.dump(nat_triggers, nat)
        json.dump(group_triggers, group)


def collect_triggers(file, dictionary):
    '''
    helper function for collecting the triggers for all idea sets in a given ideaset file and then returning a
    dictionary.
    '''
    with open(file, 'r') as t:
        clauseIdeas = ClauseWizard.cwparse(t.read())
        ideasJson = ClauseWizard.cwformat(clauseIdeas)
        for ideaName, ideaSet in ideasJson.items():
            if "trigger" in ideaSet:
                dictionary[ideaName] = ideaSet["trigger"]
            else:
                dictionary[ideaName] = {}
    return dictionary

def load_triggers(filepath):
    triggerMap = {}
    with open(filepath) as f:
        triggerJson = json.load(f)
        for ideaName, trigger in triggerJson.items():
            triggerMap[ideaName] = Trigger(trigger)
    return triggerMap

def load_country(file):
    country_tree = parse_txt_file(file)
    return country_tree