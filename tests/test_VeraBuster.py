import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest

from VeraBuster import linuxCrack, printProgressBar, check_root

def test_linuxCrack_success():
    result = linuxCrack("valid_password", "veracrypt", "/path/to/volume", 1, 1, debug=True)
    assert result == True

def test_linuxCrack_failure():
    result = linuxCrack("invalid_password", "veracrypt", "/path/to/volume", 1, 1, debug=True)
    assert result == False

def test_printProgressBar():
    printProgressBar(1, 10)

def test_check_root_with_root_privileges():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_root()
    assert pytest_wrapped_e.type == SystemExit

def test_check_root_without_root_privileges():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        check_root()
    assert pytest_wrapped_e.type == SystemExit