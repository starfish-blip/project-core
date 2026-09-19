from config import Config

def test_config():
    assert Config.VERSION == "1.0.0"
    assert isinstance(Config.DEBUG, bool)
