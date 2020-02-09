import pyradox

encodings = ['cp1252', 'utf_8_sig']


def parse_txt_file(file):
    '''
    Use pyradox's parser methods to parse a paradox file.
    '''
    game_string = pyradox.txt.readlines(file, encodings)
    token_data = pyradox.txt.lex(game_string, file)
    token_tree = pyradox.txt.parse_tree(token_data, file)
    return token_tree
