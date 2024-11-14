import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from seamstress import distribute_seamstress_work

def test_distribute_seamstress_work():
    seamstresses = [
        {'sleeve': 10, 'collar': 5, 'button': 5},
        {'sleeve': 12, 'collar': 10, 'button': 8},
        {'sleeve': 15, 'collar': 8, 'button': 8},
        {'sleeve': 9, 'collar': 7, 'button': 10},
        {'sleeve': 9, 'collar': 12, 'button': 10},
    ]

    pieces = {
        'sleeve': 150,
        'collar': 150,
        'button': 150,
    }

    avaliable_time = 180

    result = distribute_seamstress_work(seamstresses, pieces, avaliable_time)

    total_sleeves = sum(d['sleeve'] for d in result)
    total_collars = sum(d['collar'] for d in result)
    total_buttons = sum(d['button'] for d in result)

    assert total_sleeves <= 150
    assert total_collars <= 150
    assert total_buttons <= 150

    assert total_sleeves > 0 or total_collars > 0 or total_buttons > 0

    seamstress_times = [0] * len(seamstresses)
    for i, allocation in enumerate(result):
        seamstress = seamstresses[i]
        seamstress_times[i] += allocation['sleeve'] * seamstress['sleeve']
        seamstress_times[i] += allocation['collar'] * seamstress['collar']
        seamstress_times[i] += allocation['button'] * seamstress['button']

    assert all(time <= avaliable_time for time in seamstress_times)


def test_zero_available_time():
    seamstresses = [
        {'sleeve': 10, 'collar': 5, 'button': 5},
    ]

    pieces = {
        'sleeve': 10,
    }

    avaliable_time = 0

    result = distribute_seamstress_work(seamstresses, pieces, avaliable_time)

    assert all(allocation['sleeve'] == 0 for allocation in result)


def test_zero_piece_parts():
    seamstresses = [
        {'sleeve': 10, 'collar': 5, 'button': 5},
    ]

    pieces = {
        'sleeve': 0,
    }

    avaliable_time = 10

    result = distribute_seamstress_work(seamstresses, pieces, avaliable_time)

    assert all(allocation['sleeve'] == 0 for allocation in result)


def test_insufficient_time():
    seamstresses = [
        {'sleeve': 10, 'collar': 5, 'button': 5},
    ]

    pieces = {
        'sleeve': 10,
	}

    avaliable_time = 5

    result = distribute_seamstress_work(seamstresses, pieces, avaliable_time)

    assert all(allocation['sleeve'] == 0 for allocation in result)


def test_extreme_seamstress_times():
    seamstresses = [
        {'sleeve': 1, 'collar': 1, 'button': 1},
        {'sleeve': 100, 'collar': 100, 'button': 100},
    ]

    pieces = {
        'sleeve': 50,
        'collar': 50,
        'button': 50,
	}

    avaliable_time = 5000

    result = distribute_seamstress_work(seamstresses, pieces, avaliable_time)

    assert sum(d['sleeve'] for d in result) == 50
    assert sum(d['collar'] for d in result) == 50
    assert sum(d['button'] for d in result) == 50
