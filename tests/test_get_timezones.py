# -*- coding: utf-8 -*-

import os
import pytxdata

fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'tz')


def test_get_timezones():
    zones = pytxdata.get_timezones()

    assert 'America/New_York' in zones
    assert 'America/Argentina/Buenos_Aires' in zones


def test_get_timezones_custom_path():
    pytxdata.set_directory(fixtures_path)

    zones = pytxdata.get_timezones()

    assert 'America/New_York' not in zones
    assert 'Europe/Paris' in zones

    pytxdata.set_directory()
