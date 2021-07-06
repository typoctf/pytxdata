# -*- coding: utf-8 -*-

import os
import pytest
from pytxdata import set_directory, tz_path, TimezoneNotFound


fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'tz')


def setup_module(module):
    if 'pytxdata_TZDATADIR' in os.environ:
        del os.environ['pytxdata_TZDATADIR']

    set_directory()


def teardown_module(module):
    if 'pytxdata_TZDATADIR' in os.environ:
        del os.environ['pytxdata_TZDATADIR']

    set_directory()


def test_set_directory():
    set_directory(fixtures_path)

    assert tz_path('Europe/Paris') == os.path.join(fixtures_path, 'Europe/Paris')

    with pytest.raises(TimezoneNotFound):
        tz_path('America/New_York')

    here = os.path.realpath(os.path.dirname(__file__))
    filepath = os.path.realpath(
        os.path.join(here, '..', 'pytxdata', 'zoneinfo', 'America', 'New_York')
    )

    set_directory()

    assert tz_path('America/New_York') == filepath


def test_env_variable():
    os.environ['pytxdata_TZDATADIR'] = fixtures_path
    set_directory()

    assert tz_path('Europe/Paris') == os.path.join(fixtures_path, 'Europe/Paris')

    with pytest.raises(TimezoneNotFound):
        tz_path('America/New_York')

    del os.environ['pytxdata_TZDATADIR']

    here = os.path.realpath(os.path.dirname(__file__))
    filepath = os.path.realpath(
        os.path.join(here, '..', 'pytxdata', 'zoneinfo', 'America', 'New_York')
    )

    set_directory()

    assert tz_path('America/New_York') == filepath
