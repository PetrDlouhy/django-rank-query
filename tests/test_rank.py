#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-rank-query
------------

Tests for `django-rank-query` models module.
"""

from django.contrib.auth.models import User
from django.test import TestCase

from model_mommy import mommy

from rank import DenseRank, Rank, UpperRank


class TestRank(TestCase):

    def setUp(self):
        mommy.make("User", last_name="Foo")
        mommy.make("User", last_name="Bar")
        mommy.make("User", last_name="Bar")
        mommy.make("User", last_name="Baz")

    def test_rank(self):
        user_rank_list = User.objects.annotate(rank=Rank('last_name')).values_list('rank', 'last_name')
        expected_list = [
            (1, "Foo"),
            (2, "Baz"),
            (3, "Bar"),
            (3, "Bar"),
        ]
        self.assertListEqual(list(user_rank_list), expected_list)

    def test_upper_rank(self):
        user_rank_list = User.objects.annotate(rank=UpperRank('last_name')).values_list('rank', 'last_name')
        expected_list = [
            (4, "Bar"),
            (4, "Bar"),
            (2, "Baz"),
            (1, "Foo"),
        ]
        self.assertListEqual(list(user_rank_list), expected_list)

    def test_dense_rank(self):
        user_rank_list = User.objects.annotate(rank=DenseRank('last_name')).values_list('rank', 'last_name')
        expected_list = [
            (1, "Foo"),
            (2, "Baz"),
            (3, "Bar"),
            (3, "Bar"),
        ]
        self.assertListEqual(list(user_rank_list), expected_list)
