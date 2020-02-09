from country.country import Country
from culture.cultureLoader import load_culture_group

class Trigger:
    '''
    Class used to parse the logic for the various triggers in idea sets
    '''
    ops = ['AND', 'OR', 'NOT']
    # each keyword calls a Trigger method, which returns a boolean value
    keywords = {
        'tag': 'is_tag',
        # some triggers randomly have tag in all caps, I'm not sure why the game files are like this bc
        # I never capitalize anything during parsing.
        'TAG': 'is_tag',
        'capital_scope': 'capital_in_scope',
        'culture_group': 'is_culture_group',
        'primary_culture': 'is_primary_culture',
        'religion_group': 'is_religion_group'
    }

    def __init__(self, triggerDict):
        self.trigger = triggerDict

    def __str__(self):
        return str(self.trigger)

    def evaluate(self, country):
        '''
        given a country and an idea_set trigger, evaluate if the country's starting position triggers the idea set
        '''
        if self.trigger:
            return self._evaluate_triggers(self.trigger, country)
        else:
            # no triggers means any country satisfies the ideaSet
            return True

    def _evaluate_triggers(self, triggerDict, country):
        # at the top level, every trigger must be satisfied.
        for trigger in triggerDict:
            if trigger in self.keywords:
                if not getattr(self, self.keywords[trigger])(triggerDict[trigger], country):
                    return False
            elif trigger in self.ops:
                if trigger == "AND":
                    levelDown = triggerDict[trigger]
                    for trigger, triggerVal in levelDown.items():
                        if not self._evaluate_triggers({trigger: triggerVal}, country):
                            return False
                    return True
                elif trigger == "NOT":
                    return not self._evaluate_triggers(triggerDict[trigger], country)
                elif trigger == "OR":
                    levelDown = triggerDict[trigger]
                    for trigger, triggerVal in levelDown.items():
                        if self._evaluate_triggers({trigger: triggerVal}, country):
                            return True
                    return False

            else:
                return False
        return True

    def is_tag(self, triggers, country):
        '''
        verify the trigger's tag requirements matches the country tag
        '''
        # two cases, either we get a list of tags or a string tag.
        if isinstance(triggers, list):
            # the tag can match any tag in the list
            return country.get_tag() in triggers
        else:
            return country.get_tag() == triggers

    def capital_in_scope(self, triggers, country):
        return False

    def is_culture_group(self, triggers, country):
        if country.primary_culture is None:
            return False
        if isinstance(triggers, list):
            for culture_group in triggers:
                cultures = load_culture_group(culture_group)
                return country.get_primary_culture() in cultures
        else:
            cultures = load_culture_group(triggers)
            return country.get_primary_culture() in cultures

    def is_primary_culture(self, triggers, country):
        if country.primary_culture is None:
            return False
        if isinstance(triggers, list):
            return country.get_primary_culture() in triggers
        return country.get_primary_culture() == triggers

    def is_religion_group(self, triggers, country):
        return False