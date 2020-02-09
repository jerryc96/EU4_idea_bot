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
    culture_groups = {}
    culture_tree = parse_txt_file(culture_game_file)
    for group_name, group_data in culture_tree.items():
        culture_groups[group_name] = []
        for culture in group_data:
            if culture not in culture_keywords:
                culture_groups[group_name].append(culture)

    with open(culture_json, 'w') as w:
        json.dump(culture_groups, w)


def load_culture_group(group_name):
    '''
    find a specific culture group from culture.json and return it
    '''
    with open(culture_json, 'r') as f:
        culture_groups = json.load(f)
        if group_name in culture_groups:
            return culture_groups[group_name]
        return None
