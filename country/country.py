class Country:
    '''
    class to represent a country's starting information, as seen in the EU4 history folder.

    country will contain their tag, capital location, religion, government and primary culture.
    '''

    def __init__(self, tag):
        self.tag = tag

    def get_tag(self):
        return self.tag