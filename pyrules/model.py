from .utility import EnumProxy

from typing import NamedTuple, List, Dict, Any, Union, Optional
from enum import Enum

Record = Dict[str, Any]


class TransformOperator(Enum):
    eq = 'assign'
    rm = 'delete'
    mv = 'move'
    cp = 'copy'

    add = 'add'
    mul = 'multiply'
    sub = 'subtract'
    div = 'divide'
    inc = 'increment'
    dec = 'decrement'

    replace = 'replace'


class LogicalOperator(Enum):
    eq = 'equal'
    lt = 'less'
    le = 'less-equal'
    gt = 'greater'
    ge = 'greater-equal'
    ne = 'not-equal'


class JunctionOperator(Enum):
    o = 'or'
    a = 'and'
    n = 'not'


Operator = EnumProxy(TransformOperator, LogicalOperator, JunctionOperator)


class Operand:
    pass


class Transform(NamedTuple):
    operator: TransformOperator
    field: Optional[str] = None
    value: Optional[Any] = None
    source: Optional[str] = None
    target: Optional[str] = None
    key: Optional[str] = None

    @staticmethod
    def from_dict(metadata: Dict) -> 'Transform':
        return Transform(operator=TransformOperator(metadata['transform']))


class Condition(NamedTuple):
    operator: Union[LogicalOperator, JunctionOperator]
    operands: List[Operand]

    @staticmethod
    def from_dict(metadata: Dict) -> 'Condition':
        op = metadata.get('operator')
        return Condition(operator=LogicalOperator.eq, operands=[])


class Rule(NamedTuple):
    transform: Transform
    condition: Optional[Condition] = None

    @staticmethod
    def from_dict(metadata: Dict) -> 'Rule':
        transform_keys = set(metadata.keys())
        condition_metadata = metadata.get('condition')
        transform_keys.discard('condition')
        transform_metadata = {key: metadata[key] for key in transform_keys}
        return Rule(transform=Transform.from_dict(transform_metadata),
                    condition=Condition.from_dict(condition_metadata) if condition_metadata else None)
