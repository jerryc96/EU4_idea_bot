import json
from utils import *

# keywords seen in religion.txt, that are not related to the names of religions
religion_keywords = ['defender_of_faith',
                     'can_form_personal_unions',
                     'center_of_religion',
                     'flags_with_emblem_percentage',
                     'flag_emblem_index_range',
                     'ai_will_propagate_through_trade',
                     'religious_schools',
                     'harmonized_modifier',
                     'crusade_name']

religion_json = './data/religion.json'

religion_game_file = './common/religions/00_religion.txt'

def store_religions():
    '''
    stores the different religion groups and their members in JSON
    '''
    store_keys_in_json(religion_keywords, religion_json, religion_game_file)

def load_religion_group(group_name):
    return load_group(group_name, religion_json)

