# -*- coding: utf-8 -*-

from pytxdata import set_directory


def setup_module(module):
    set_directory()


def teardown_module(module):
    set_directory()
