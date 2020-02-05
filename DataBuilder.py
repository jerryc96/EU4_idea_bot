import re
import ClauseWizard

tagFile = './common/country_tags/00_countries.txt'
uniqueIdeasFile = ['./common/ideas/00_country_ideas.txt']

# for group ideas and generic ideas
genericIdeasFile = ['./common/ideas/zz_group_ideas.txt', './common/ideas/zzz_default_idea.txt',
                    './common/ideas/00_basic_ideas.txt']

ideasTokens = './idea_tokens.txt'

def gen_tag_library():
    '''
    Generate the list of country tags in EU4, found in common/country_tags
    '''
    tagMap = {}

    with open(tagFile) as t:
        data = t.readlines()
        for line in data:
            # check for comments
            if '=' in line and line[0] != '#':
                tag = line[0:3]
                countryNameSearch = re.search('countries/(.*)\.txt', line)
                if countryNameSearch:
                    countryName = countryNameSearch.group(1)
                    tagMap[tag] = countryName
            else:
                continue
    return tagMap

def gen_country_ideas_library(tagLib):
    '''
    Generate a dict of all idea sets

    Since many national ideas are displayed in common as tags, we need to parse them and return the country name

    EU4 stores its idea sets in three different files as of this moment, so we need to grab each file from the
    file location and collect the ideasets
    '''
    # print(tagLib)
    ideasLib = {}
    for file in uniqueIdeasFile:
        add_ideas(file, ideasLib, tagLib)

    for genfile in genericIdeasFile:
        add_generic_ideas(genfile, ideasLib, tagLib)
    return ideasLib

def add_ideas(file, dictionary, tagLib):
    '''
    add the ideasets from an idea group file into the general library.
    '''
    with open(file, 'r') as t:
        clauseIdeas = ClauseWizard.cwparse(t.read())
        ideasJson = ClauseWizard.cwformat(clauseIdeas)
        for ideaName, ideaSet in ideasJson.items():
            ideaTag = re.search('(.*)_(.*)', ideaName)
            if ideaTag.group(1) in tagLib:
                ideaName = tagLib[ideaTag.group(1)]
            dictionary[ideaName] = ideaSet
    return dictionary

def add_generic_ideas(file, dictionary, tagLib):
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