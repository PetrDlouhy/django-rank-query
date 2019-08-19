from django.db.models import Func

__version__ = '0.1.0'


class Rank(Func):
    function = 'RANK'
    template = '%(function)s() OVER (ORDER BY %(expressions)s DESC)'


class AscRank(Func):
    """Rank items in ascending order."""
    function = 'RANK'
    template = '%(function)s() OVER (ORDER BY %(expression)s ASC)'


class DenseRank(Func):
    function = 'DENSE_RANK'
    template = '%(function)s() OVER (ORDER BY %(expressions)s DESC)'


class UpperRank(Func):
    function = 'RANK'
    template = 'COUNT(*) OVER () + 1 - %(function)s() OVER (ORDER BY %(expressions)s ASC)'
