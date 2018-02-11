from typing import Dict, Any, Set, DefaultDict
from enum import Enum


class EnumProxy:

    def __init__(self, *args):
        self.lookup: Dict[Any, Enum] = dict()
        self.reverse_lookup: DefaultDict[str, Set[Any]] = DefaultDict(set)

        for cls in args:
            if hasattr(cls, '__members__'):
                for k, e in cls.__members__.items():
                    self.lookup[e.value] = e
                    self.reverse_lookup[k].add(e)
            else:
                raise ValueError(dict(message='parameter must be enum', param=cls))

    def __call__(self, name):
        return self.lookup[name]

    def __getitem__(self, item):
        s = self.reverse_lookup[item]
        if len(s) == 1:
            return list(s)[0]
        # TODO: edge cases
