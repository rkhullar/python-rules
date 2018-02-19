from typing import Any, Set, DefaultDict
from enum import Enum


class EnumProxy:

    def __init__(self, *args):
        self.value_lookup: DefaultDict[Any, Set[Enum]] = DefaultDict(set)
        self.name_lookup: DefaultDict[str, Set[Enum]] = DefaultDict(set)
        self.enum_names: Set[str] = set()

        for cls in args:
            if hasattr(cls, '__members__'):
                self.enum_names.add(cls.__name__)
                for k, e in cls.__members__.items():
                    v = e.value
                    self.value_lookup[v].add(e)
                    self.name_lookup[k].add(e)
            else:
                raise ValueError(dict(message='parameter must be enum', param=cls))

    def __call__(self, value: Any):
        if value not in self.value_lookup:
            raise ValueError(dict(message='no such value for enums', value=value, enums=self.enum_names))
        enum_set = self.value_lookup[value]
        if len(enum_set) == 1:
            return list(enum_set)[0]
        else:
            raise Exception(dict(message='multiple enums found for value', value=value, enums=self.enum_names))

    def __getitem__(self, name: str):
        if name not in self.name_lookup:
            raise ValueError(dict(message='no such name for enums', name=name, enums=self.enum_names))
        enum_set = self.name_lookup[name]
        if len(enum_set) == 1:
            return list(enum_set)[0]
        else:
            raise Exception(dict(message='multiple enums found for name', name=name, enums=self.enum_names))
