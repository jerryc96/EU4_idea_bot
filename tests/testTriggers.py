import unittest
from triggers.trigger import Trigger
from country.country import Country

class TestTrigger(unittest.TestCase):

    rus = Country('RUS')
    pru = Country('PRU')
    bra = Country('BRA')

    trigger_dict = {
        'tag': 'RUS'
    }
    or_trigger_dict = {
        'OR': {
            'tag': ['RUS', 'PRU']
        }
    }

    not_trigger_dict = {
        'NOT': {
            'tag': 'PRU'
        }
    }

    combo_trigger_dict = {
        'NOT': {
            'OR': {
                'tag': ['RUS', 'PRU']
            }
        }
    }

    trigger = Trigger(trigger_dict)
    or_trigger = Trigger(or_trigger_dict)
    not_trigger = Trigger(not_trigger_dict)
    combo_trigger = Trigger(combo_trigger_dict)

    def test_match_tag(self):
        self.assertTrue(self.trigger.evaluate(self.rus))
        self.assertFalse(self.trigger.evaluate(self.pru))

    def test_OR_keyword(self):
        self.assertTrue(self.or_trigger.evaluate(self.rus))
        self.assertTrue(self.or_trigger.evaluate(self.pru))
        self.assertFalse(self.or_trigger.evaluate(self.bra))

    def test_NOT_keyword(self):
        self.assertFalse(self.not_trigger.evaluate(self.pru))
        self.assertTrue(self.not_trigger.evaluate(self.rus))

    def test_combo_keyword(self):
        self.assertFalse(self.combo_trigger.evaluate(self.rus))
        self.assertTrue(self.combo_trigger.evaluate(self.bra))