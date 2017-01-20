# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from rank.urls import urlpatterns as rank_urls

urlpatterns = [
    url(r'^', include(rank_urls, namespace='rank')),
]
