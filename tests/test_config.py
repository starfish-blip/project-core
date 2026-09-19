import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from config import Config

def test_config():
    assert Config.VERSION == "1.0.0"
    assert isinstance(Config.DEBUG, bool)
