""" test main flows of metavox"""

import os
import tempfile
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
    slide_0_notes = "MetaVox is a groundbreaking AI-driven"
    file_path = get_resource_path("dummy_presentation", "pptx")
    presentation = pt.read_presentation(file_path)

    assert presentation is not None
    assert len(presentation.slides) == 4
    assert slide_0_notes in pt.get_speaker_notes(presentation, 0)


def test_libreoffice_version():
    """test presentation load"""
    version = pt.get_libreoffice_version()
    assert version is not None
    file_path = get_resource_path("dummy_presentation", "pptx")
    _, file_name = os.path.split(file_path)
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Convert the PPTX file to PDF
        output = pt.convert_pptx_to_pdf(file_path, temp_dir)
        assert output is not None
        assert os.path.exists(output)
        assert os.path.splitext(file_name)[0] + ".pdf" in os.listdir(temp_dir)
