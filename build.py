from religion.religionLoader import store_religions
from culture.cultureLoader import store_cultures
from DataBuilder import *


# build the JSON library in ./data
if __name__ == '__main__':
    store_religions()
    store_cultures()
    store_triggers()
    print('done')