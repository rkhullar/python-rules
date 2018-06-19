from . import Record, RecordValue, Operand
from .operators import *
from typing import NamedTuple, Optional, List, Union


class Transform(NamedTuple):
    operator: TransformOperator
    source: Optional[str] = None
    target: Optional[str] = None
    search: Optional[str] = None
    value: Optional[RecordValue] = None

    @staticmethod
    def from_dict(metadata: Record) -> 'Transform':
        params = dict(metadata)
        params['operator'] = params.pop('transform', None)
        return Transform(**params)


class Condition(NamedTuple):
    operator: Union[LogicalOperator, JunctionOperator]
    operands: List[Operand]

    @staticmethod
    def from_dict(metadata: Record) -> 'Condition':
        op = metadata.get('operator')
        return Condition(operator=LogicalOperator.eq, operands=[])


class Rule(NamedTuple):
    transform: Transform
    condition: Optional[Condition] = None

    @staticmethod
    def from_dict(metadata: Record) -> 'Rule':
        transform_keys = set(metadata.keys())
        condition_metadata = metadata.get('condition')
        transform_keys.discard('condition')
        transform_metadata = {key: metadata[key] for key in transform_keys}
        return Rule(transform=Transform.from_dict(transform_metadata),
                    condition=Condition.from_dict(condition_metadata) if condition_metadata else None)
