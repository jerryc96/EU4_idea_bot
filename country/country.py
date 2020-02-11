
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
        self.technology_group = country_tree['technology_group'] if 'technology_group' in country_tree else None
        self.government = country_tree['government'] if 'government' in country_tree else None
        self.govt_reforms = country_tree['add_government_reform'] if 'add_government_reform' in country_tree else None

    def __repr__(self):
        result = f"tag: {self.tag} \n Government: {self.government} \n primary_culture: {self.primary_culture}\n" +\
                 f"religion: {self.religion} \n capital: {self.capital}\n tech_group: {self.technology_group}\n"
        return result

    def get_tag(self):
        return self.tag

    def get_primary_culture(self):
        return self.primary_culture

    def get_religion(self):
        return self.religion

    def get_government(self):
        return self.government

    def get_govt_reforms(self):
        return self.govt_reforms

    def get_tech_group(self):
        return self.technology_group