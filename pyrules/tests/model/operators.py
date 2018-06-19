from enum import Enum


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
