from ..model import *
import unittest


class ModelTester(unittest.TestCase):

    def test_enums(self):
        self.assertEqual(TransformOperator['eq'], TransformOperator('assign'))
