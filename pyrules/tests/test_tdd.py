import unittest

from typing import Generator, List

from .model import *


def build_rule_from_dict(definition: Dict) -> Rule:
    return Rule(transform=Transform(definition['transform']))


class RuleEngine(Generator):
    def __init__(self, rules: List[Rule]=list()):
        self.rules = rules

    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration

    def send(self, data: Record) -> Record:
        return data


class ScratchTester(unittest.TestCase):

    # def test1(self):
    #     json_rule = dict(transform='assign', field='x', value=1)
    #     engine = RuleEngine(rules=[build_rule_from_dict(json_rule)])
    #     x = dict()
    #     e = dict(x=1)
    #     y = engine.send(x)
    #     self.assertEqual(e, y)

    def test2(self):

        self.assertRaises(Exception, lambda: Operator['eq'])
        self.assertEqual(Operator('assign'), TransformOperator.eq)
        self.assertEqual(Operator['add'], TransformOperator.add)
        self.assertEqual(Operator('or'), JunctionOperator.o)
