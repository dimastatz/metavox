""" test main flows of metavox"""

import metavox


def test_version():
    """test version"""
    assert metavox.__version__ == "0.1.0"
