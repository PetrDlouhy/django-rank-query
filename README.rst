=============================
rank
=============================

.. image:: https://badge.fury.io/py/django-rank-query.svg
    :target: https://badge.fury.io/py/django-rank-query

.. image:: https://travis-ci.org/petrdlouhy/django-rank-query.svg?branch=master
    :target: https://travis-ci.org/petrdlouhy/django-rank-query

.. image:: https://codecov.io/gh/petrdlouhy/django-rank-query/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/petrdlouhy/django-rank-query

**Warning:** Since Django 2.0 this application is deprecated. Use built in `window functions <https://docs.djangoproject.com/en/2.0/ref/models/database-functions/#window-functions>`_.

Enable SQL Window functions for use in Django queries. Add rank to your query.

Django in curren't version (1.10) doesn't support `window functions <https://www.postgresql.org/docs/9.3/static/functions-window.html>`_ as seen in PostgreSQL.
This implemets `rank`, `dense_rank` and adds shortcut for `upper_rank`, which retrieves upper value for rank (rank of last element in the window).
The implementation is currently working only on PostgreSQL.

Note: The support for window functions is being already solved in `issue #26608 <https://code.djangoproject.com/ticket/26608>`_.

Quickstart
----------

Install rank::

    pip install django-rank-query

Usage
-----


U can annotate users by rank (sequenc number in alphabet) of their
last name the like this::

    from rank import DenseRank, UpperRank, Rank
    users = User.objects.all()
    users = user.annotate(lower_rank=Rank('last_name'))
    users = user.annotate(upper_rank=UpperRank('last_name'))
    users = user.annotate(dense_rank=DenseRank('last_name'))

Then you have user query annotated with various ranks. You can retrieve them for example by `values` function::

   user_ranks = users.values('last_name', 'lower_rank', 'upper_rank')

Note: PostgreSQL doesn't support combining `rank` functions with `GROUP_BY` or in `WHERE` clause. So you cannot use them in aggregation queries.

Rank is counted in the current `select` query, so filtering will change rank of given elements, so you can't have sequence number in whole table filtered by ie. his name.
This can be solved by using subqueries in SQL, but Django doesn't support them as far as I know.


Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
