from ...utility.enum_proxy import EnumProxy
from enum import Enum
import unittest


class EnumProxyTester(unittest.TestCase):

    def test_one(self):

        class A(Enum):
            x = 1

        class B(Enum):
            x = 1

        AB = EnumProxy(A, B)

        self.assertEqual({'A', 'B'}, AB.enum_names)

