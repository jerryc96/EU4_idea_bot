from modifier.modifierList import ModifierList
'''
Different modifiers are displayed differently by EU4.

for example, tax modifier is done in percentages, but inflation is done with a flat rate. This file seeks to consolidate
and track that so it's what you see when it's displayed in-game.
'''

class BaseModifier:
    '''
    Base class outlining how to parse EU4 modifiers as presented in the common folder
    '''
    name = ""
    effect = ""

    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


class PercentModifier(BaseModifier):
    '''
    Class for handling modifiers that are percent based. I.e. National Tax, Discipline, Morale, etc.
    '''

    def __str__(self):
        if not isinstance(self.effect, float):
            raise TypeError("effect must be a number")
        elif self.effect > 0:
            return f'{self.name}: +{self.effect * 100}% \n'
        else:
            return f'{self.name}: {self.effect * 100}% \n'


class FloatModifier(BaseModifier):
    '''
    Class for handling modifiers that increase/decrease monthly but ARE NOT DISPLAYED AS PERCENTS. I.e.
    Inflation Reduction, Prestige, etc.
    '''

    def __str__(self):
        if not isinstance(self.effect, float):
            raise TypeError("effect must be a number")
        elif self.effect > 0:
            return f'{self.name}: +{self.effect} \n'
        else:
            return f'{self.name}: {self.effect} \n'

class IntegerModifier(BaseModifier):
    '''
    Class for handling modifiers that are displayed as Integers. I.E diplomats, leaders, etc.
    '''
    def __str__(self):
        if not isinstance(self.effect, int):
            raise TypeError("effect must be a number")
        elif self.effect > 0:
            return f'{self.name}: +{self.effect} \n'
        else:
            return f'{self.name}: {self.effect} \n'

class BooleanModifier(BaseModifier):
    '''
    Class for modifiers that allow the country to perform a certain action.
    I.e. May Raid Coasts, Siberian Frontiers, etc.
    '''

    def __str__(self):
        return f'{self.name} \n'

def modifier_factory(modifierType, name, effect):
    if modifierType == 'BooleanModifier':
        return BooleanModifier(name, effect)
    elif modifierType == 'FloatModifier':
        return FloatModifier(name, float(effect))
    elif modifierType == 'PercentModifier':
        return PercentModifier(name, float(effect))
    elif modifierType == 'IntegerModifier':
        return IntegerModifier(name, int(effect))
    raise ValueError("Not a valid modifier effect")

def modifier_from_dict(idea):
    '''
    The ideas in IdeaGroup object are stored in dictionaries.

    Converts it into a list of modifiers.
    '''
    modifiers = []
    for name, effect in idea.items():
        try:
            modEnum = ModifierList[name].value
            modifier = modifier_factory(modEnum[0], modEnum[1], effect)
            modifiers.append(modifier)
        except KeyError:
            raise KeyError(f'{name} not in modifier list. need to update')
    return modifiers
