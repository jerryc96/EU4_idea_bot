from modifier.modifiers import modifier_from_dict
import mdFormatter as md
from ideaGroup.outliers import repeatedIdeaNames

class ideaGroup:
    '''
    Class to represent Idea Group
    '''
    # special keys in the ideaSet object
    keywords = ['free', 'trigger', 'start', 'bonus', 'ai_will_do', 'category', 'important']
    boundaryCase = {
        "ghazi": {
            "manpower_recovery_speed": "0.2"
        },
        "french_language_in_all_courts": {
            "diplomatic_upkeep": "1"
        },
        "chagatai_literature": {
            "legitimacy": "1",
            "horde_unity": "1"
        },
        "reform_the_diwan": {
            "yearly_corruption": "-0.1"
        },
        "in_honor_of_ali": {
            "tolerance_heretic": "3"
        },
        "coffea_arabica": {
            "global_trade_power": "0.1"
        },
        "dakani_language": {
            "num_accepted_cultures": "1"
        },
        "life_of_steppe_warrior": {
            "land_attrition": "-0.20"
        },
        "glory_of_conquest": {
            "global_manpower_modifier": "0.25"
        },
        "zaz_steppe_riders": {
            "land_attrition": "-0.15"
        },
        "marwari_horses": {
            "cavalry_power": "0.15",
            "movement_speed": "0.1"
        },
        "jute_production": {
            "production_efficiency": "0.1"
        },
        "tradition_of_conquest": {
            "core_creation": "-0.25"
        },
        "logistics_of_khan": {
            "manpower_recovery_speed": "0.2"
        },
        "lao_ethnic_diversity": {
            "num_accepted_cultures": "1"
        },
        "malagasy_pirate_ports": {
            "embargo_efficiency": "0.1",
            "privateer_efficiency": "0.15"
        },
        "zambezi_maravi_influences": {
            "stability_cost_modifier": "-0.1"
        },
        "securing_defenses_central_indic": {
            "defensiveness": "0.15"
        },
        "merchants_of_southern_india": {
            "trade_range_modifier": "0.20"
        }
    }
    name = ''
    triggers = []

    def __init__(self, ideaGroupName, ideaSet):
        self.name = ideaGroupName
        self.tradition = (modifier_from_dict(ideaSet['start']))
        self.ambition = (modifier_from_dict(ideaSet['bonus']))
        # certain ideaSets have specific triggers that allow a nation to take the set.
        # may be useful to someone else who wishes to improve the bot
        self.national_set = []
        if 'trigger' in ideaSet:
            self.triggers = self._find_triggers(ideaSet['trigger'])
        for key, value in ideaSet.items():
            if key not in self.keywords:
                if key in repeatedIdeaNames:
                    self.national_set.append({key: modifier_from_dict(self.boundaryCase[key])})
                else:
                    try:
                        self.national_set.append({key: modifier_from_dict(value)})
                    except KeyError as e:
                        # this usually means a modifier wasn't in ModifierList. The Bot will then notify the maintainer
                        raise e
                    except AttributeError as err:
                        # this error means some ideaset uses a duplicate idea name from a different ideaset.
                        # paradox will normally comment this out when it's repeated to save lines, which lead to
                        # and empty string when fetching the idea's effects.
                        print(key)
                        print(self.name)
                        print(err)
        self.national_set = tuple(self.national_set)

    def _find_triggers(self, triggers):
        '''
        find the triggers that allow a country to adopt the given idea set, return array of tags that match the trigger
        '''
        # ideas sets with multiple tags are always under 'OR' key
        if 'OR' in triggers:
            return triggers['OR']['tag']
        elif 'tag' in triggers:
            return [triggers['tag']]
        return []

    def to_comment(self):
        result = f'{md.header(self.name + " Ideas")}\n'
        result += f'{md.bold("Traditions:")} \n\n'
        for mod in self.tradition:
            result += f'{str(mod)} \n'
        for idea in self.national_set:
            for name, mod in idea.items():
                result += f'{md.bold(name)}:\n\n'
                for modifier in mod:
                    result += f'{modifier} \n'
        result += f'{md.bold("Ambition:")} \n\n'
        for mod in self.ambition:
            result += f'{str(mod)} \n'
        return result

    def __str__(self):
        result = f'idea name: {self.name} \n'
        for mod in self.tradition:
            result += f'{str(mod)} \n'
        for mod in self.ambition:
            result += f'{str(mod)} \n'
        print(self.national_set)
        for idea in self.national_set:
            for name, mod in idea.items():
                result += f'{name}:\n'
                for modifier in mod:
                    result += f'{modifier} \n'
        return result

    def __repr__(self):
        return f'{self.name}: {self.tradition}'

    def get_name(self):
        return self.name

    def get_tradition(self):
        return self.tradition

    def get_ambition(self):
        return self.ambition

    def get_set(self):
        return self.national_set