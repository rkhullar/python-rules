from typing import NamedTuple, List, Dict, Any, Union, Optional
from enum import Enum


class TransformOperator(Enum):
    eq = 'assign'
    rm = 'delete'
    mv = 'move'
    cp = 'copy'

    add = 'add'
    mul = 'muliply'
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


class Operand:
    pass


class Transform(NamedTuple):
    operator: TransformOperator
    field: Optional[str] = None
    value: Optional[Any] = None
    source: Optional[str] = None
    target: Optional[str] = None
    key: Optional[str] = None


class Condition(NamedTuple):
    operator: Union[LogicalOperator, JunctionOperator]
    operands: List[Operand]


class Rule(NamedTuple):
    transform: Transform
    condition: Optional[Condition] = None


t = Transform(operator=TransformOperator.eq)
print(t)

