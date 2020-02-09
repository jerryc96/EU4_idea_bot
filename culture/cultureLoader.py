import glob
import ClauseWizard
import json

# keywords seen in culture.txt, that are not related to primary cultures
cultureKeywords = ['graphical_culture', 'male_names', 'female_names', 'dynasty_names']

# a place to store the relevant sections in the game files
cultureJson = "./data/culture.json"

cultureGameFile = "./common/cultures/00_cultures.txt"

def store_cultures():
    '''
    the actual game file for culture contains culture groups, cultures, and other information not needed for
    trigger based calculations.

    isolates and dumps cultures and their culture groups into a JSON file.
    '''
    culturePrimaries = {}
    with open(cultureGameFile, 'r', encoding="iso8859_1") as f:
        parsedFile = ClauseWizard.cwparse(f.read())
        cultureDict = ClauseWizard.cwformat(parsedFile)

        for group_name, cultures in cultureDict.items():
            group = []
            for culture in cultures:
                if culture not in cultureKeywords:
                    group.append(culture)
            culturePrimaries[group_name] = group

    with open(cultureJson, 'w') as w:
        json.dump(culturePrimaries, w)


def culture_parser():
    '''
    self made parser based on clausewizard to parse the culture file in EU4. Last resort
    '''
    pass