import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from core import initialize_system

def test_initialize_system():
    assert initialize_system() is True
