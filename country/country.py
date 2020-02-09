
class Country:
    '''
    class to represent a country's starting information, as seen in the EU4 history folder.

    country will contain their tag, capital location, religion, government and primary culture.
    '''

    def __init__(self, tag, country_tree):
        self.tag = tag
        self.government = country_tree['government'] if 'government' in country_tree else None
        self.primary_culture = country_tree['primary_culture'] if 'primary_culture' in country_tree else None
        self.religion = country_tree['religion'] if 'religion' in country_tree else None
        self.capital = country_tree['capital'] if 'capital' in country_tree else None

    def __repr__(self):
        result = f"tag: {self.tag} \n Government: {self.government} \n primary_culture: {self.primary_culture}\n" +\
                 f"religion: {self.religion} \n capital: {self.capital}\n\n"
        return result

    def get_tag(self):
        return self.tag

    def get_primary_culture(self):
        return self.primary_culture

    def get_religion(self):
        return self.religion