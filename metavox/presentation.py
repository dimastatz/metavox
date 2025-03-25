"""Document class for handling the document file"""

from io import BytesIO
from pptx import Presentation


def read_presentation(file_path) -> Presentation:
    """Read the presentation from the document file"""
    with open(file_path, "rb") as file:
        source_stream = BytesIO(file.read())
        return Presentation(source_stream)


def get_speaker_notes(presentation: Presentation, slide_index: int) -> str:
    """Get the speaker notes from the slide"""
    slide = presentation.slides[slide_index]
    notes_slide = slide.notes_slide
    return notes_slide.notes_text_frame.text
