from modifier.modifiers import modifier_from_dict
import mdFormatter as md
from ideaGroup.outliers import repeatedIdeaNames

class ideaGroup:
    '''
    Class to represent Idea Group
    '''
    # special keys in the ideaSet object
    keywords = ['free', 'trigger', 'start', 'bonus', 'ai_will_do', 'category', 'important']
    name = ''
    triggers = []

    def __init__(self, ideaGroupName, ideaSet):
        self.name = ideaGroupName.upper()
        self.tradition = (modifier_from_dict(ideaSet['start']))
        self.ambition = (modifier_from_dict(ideaSet['bonus']))
        # certain ideaSets have specific triggers that allow a nation to take the set.
        # may be useful to someone else who wishes to improve the bot
        self.national_set = []
        for key, value in ideaSet.items():
            if key not in self.keywords:
                if key in repeatedIdeaNames:
                    self.national_set.append({key: modifier_from_dict(repeatedIdeaNames[key])})
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

    def to_comment(self):
        result = f'{md.header(self.name + " Ideas")}\n'
        if len(self.tradition) > 1:
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
        for idea in self.national_set:
            for name, mod in idea.items():
                result += f'{name}:\n'
                for modifier in mod:
                    result += f'{modifier} \n'
        return result

    def __repr__(self):
        return f'{self.name}'

    def get_name(self):
        return self.name

    def get_tradition(self):
        return self.tradition

    def get_ambition(self):
        return self.ambition

    def get_set(self):
        return self.national_set