import json
from utils import *

# keywords seen in culture.txt, that are not related to primary cultures
culture_keywords = ['graphical_culture', 'male_names', 'female_names', 'dynasty_names', 'primary']

# a place to store the relevant sections in the game files
culture_json = "./data/culture.json"

culture_game_file = "./common/cultures/00_cultures.txt"

def store_cultures():
    '''
    the actual game file for culture contains culture groups, cultures, and other information not needed for
    trigger based calculations.

    isolates and dumps cultures and their culture groups into a JSON file.
    '''
    store_keys_in_json(culture_keywords, culture_json, culture_game_file)


def load_culture_group(group_name):
    '''
    find a specific culture group from culture.json and return it
    '''
    return load_group(group_name, culture_json)
