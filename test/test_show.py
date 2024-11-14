import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import pytest
from show import show_distribution

def test_show_distribution(capfd):
    distribution = [
        {'sleeve': 50, 'collar': 40, 'button': 60},
        {'sleeve': 30, 'collar': 50, 'button': 20},
        {'sleeve': 70, 'collar': 60, 'button': 70},
    ]

    show_distribution(distribution)

    captured = capfd.readouterr()
    expected_output = (
        'seamstress 0: 50 sleeve(s), 40 collar(s), 60 button(s)\n'
        'seamstress 1: 30 sleeve(s), 50 collar(s), 20 button(s)\n'
        'seamstress 2: 70 sleeve(s), 60 collar(s), 70 button(s)\n'
    )

    assert captured.out == expected_output
