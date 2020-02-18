import pyradox
import json


encodings = ['cp1252', 'utf_8_sig']


def parse_txt_file(file):
    '''
    Use pyradox's parser methods to parse a paradox file.
    '''
    game_string = pyradox.txt.readlines(file, encodings)
    token_data = pyradox.txt.lex(game_string, file)
    token_tree = pyradox.txt.parse_tree(token_data, file)
    return token_tree


def store_keys_in_json(keywords, json_path, txt_path):
    '''
    Some mechanics, like culture and religion, have different groups with individual culture/religions belonging
    in a specific group. This function parse that file and dumps the group names and its members in JSON.
    '''
    group = {}
    token_tree = parse_txt_file(txt_path)
    for group_name, group_data in token_tree.items():
        group[group_name] = []
        for key in group_data:
            if key not in keywords:
                group[group_name].append(key)

    with open(json_path, 'w') as w:
        json.dump(group, w)


def load_group(group_name, json_path):
    with open(json_path, 'r') as f:
        groups = json.load(f)
        if group_name in groups:
            return groups[group_name]
        return None