from ...utility.enum_proxy import EnumProxy
from enum import Enum
import unittest


class EnumProxyTester(unittest.TestCase):

    def test_class_0(self):
        proxy = EnumProxy()
        self.assertEqual(set(), proxy.enum_names)

    def test_class_1(self):

        class A(Enum):
            x = 1

        proxy = EnumProxy(A)

        self.assertEqual(set('A'), proxy.enum_names)

    def test_class_2(self):

        class A(Enum):
            x = 1

        class B(Enum):
            x = 2

        proxy = EnumProxy(A, B)

        self.assertEqual(set('AB'), proxy.enum_names)

    def test_construct_non_enum(self):

        with self.assertRaises(ValueError) as context:
            EnumProxy('test-input')

        y = context.exception.args[0]
        e = dict(message='parameter must be enum', param='test-input')
        self.assertEqual(e, y)

    def test_name(self):

        class A(Enum):
            x = 1

        class B(Enum):
            y = 2

        proxy = EnumProxy(A, B)
        self.assertEqual(A.x, proxy['x'])
        self.assertEqual(B.y, proxy['y'])

    def test_name_overlap(self):

        class A(Enum):
            x = 1

        class B(Enum):
            x = 2

        proxy = EnumProxy(A, B)

        with self.assertRaises(Exception) as context:
            proxy['x']

        y = context.exception.args[0]
        e = dict(message='multiple enums found for name', name='x', enums=set('AB'))
        self.assertEqual(e, y)

    def test_value(self):

        class A(Enum):
            x = 1

        class B(Enum):
            y = 2

        proxy = EnumProxy(A, B)
        self.assertEqual(A.x, proxy(1))
        self.assertEqual(B.y, proxy(2))

    def test_value_overlap(self):

        class A(Enum):
            x = 1

        class B(Enum):
            y = 1

        proxy = EnumProxy(A, B)

        with self.assertRaises(Exception) as context:
            proxy(1)

        y = context.exception.args[0]
        e = dict(message='multiple enums found for value', value=1, enums=set('AB'))
        self.assertEqual(e, y)

    def test_unknown_name(self):

        class A(Enum):
            x = 1

        class B(Enum):
            y = 2

        proxy = EnumProxy(A, B)

        with self.assertRaises(ValueError) as context:
            proxy['z']

        y = context.exception.args[0]
        e = dict(message='no such name for enums', name='z', enums=set('AB'))
        self.assertEqual(e, y)

    def test_unknown_value(self):

        class A(Enum):
            x = 1

        class B(Enum):
            y = 2

        proxy = EnumProxy(A, B)

        with self.assertRaises(ValueError) as context:
            proxy(3)

        y = context.exception.args[0]
        e = dict(message='no such value for enums', value=3, enums=set('AB'))
        self.assertEqual(e, y)
