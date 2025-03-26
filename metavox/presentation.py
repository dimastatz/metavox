"""Document class for handling the document file"""

import os
from io import BytesIO
from pptx import Presentation
from aspose import slides


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


def slide_to_image(
    file_name: str, slide_index: int, target_folder: str, scale=1
) -> BytesIO:
    """Convert the slide to an image"""
    with slides.Presentation(file_name) as presentation:
        slide = presentation.slides[slide_index]
        with slide.get_image(scale, scale) as thumbnail:
            _, file = os.path.split(file_name)
            file = file.split(".")[0] + f"_slide_{slide_index}.jpg"
            thumbnail.save(os.path.join(target_folder, file), slides.ImageFormat.JPEG)
            return os.path.join(target_folder, file)
