""" test main flows of metavox"""

import os
import metavox
import metavox.presentation as pt


def get_resource_path(name: str, extension: str) -> str:
    "get resources path"
    current_path = os.path.dirname(__file__)
    path = os.path.join(current_path, f"./resources/{name}")
    return f"{path}.{extension}"


def test_version():
    """test version"""
    assert metavox.__version__ == "0.1.0"


def test_read_presentation():
    """test presentation load"""
    presentation = pt.read_presentation(get_resource_path("dummy_presentation", "pptx"))
    assert presentation is not None
    assert len(presentation.slides) == 4
    assert not presentation.slides[0].notes_slide.notes_text_frame.text is None
