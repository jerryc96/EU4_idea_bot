import unittest
from DataBuilder import gen_country_ideas_library, gen_non_national_ideas_library
from ideaGroup.ideaGroup import ideaGroup

class TestModifiers(unittest.TestCase):

    def test_missing_modifiers(self):
        '''
        fetch every ideaset in common,
        Try to convert it into a modifier. If any does not exist in modifier, add it to missing modifiers list.
        '''
        missingModifierList = []
        ideaDict = gen_country_ideas_library()
        nonNatIdeaDict = gen_non_national_ideas_library()

        for ideaName, ideaSet in ideaDict.items() :
            try:
                idea = ideaGroup(ideaName, ideaSet)
            except KeyError as e:
                if str(e) not in missingModifierList:
                    missingModifierList.append(str(e))
        for ideaName, ideaSet in nonNatIdeaDict.items():
            try:
                idea = ideaGroup(ideaName, ideaSet)
            except KeyError as e:
                if str(e) not in missingModifierList:
                    missingModifierList.append(str(e))
        if len(missingModifierList) > 0:
            print(missingModifierList)
            self.assertTrue(False)
        else:
            self.assertTrue(True)