""" Check version test """
from example import __version__


def test_version():
    """Versions must match in this test"""
    assert __version__ == "0.1.0"
