=====
Usage
=====

To use rank in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rank.apps.RankConfig',
        ...
    )

Add rank's URL patterns:

.. code-block:: python

    from rank import urls as rank_urls


    urlpatterns = [
        ...
        url(r'^', include(rank_urls)),
        ...
    ]
