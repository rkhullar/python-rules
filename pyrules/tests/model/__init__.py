from ...utility import EnumProxy
from .operators import TransformOperator, JunctionOperator, LogicalOperator
from .factory import Transform, Condition, Rule

from typing import Dict, Union
from decimal import Decimal

RecordValue = Union[str, int, float, Decimal, Dict]
Record = Dict[str, RecordValue]


Operator = EnumProxy(TransformOperator, LogicalOperator, JunctionOperator)


class Operand:
    pass
