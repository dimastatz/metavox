"""Document class for handling the document file"""

from pathlib import Path


class Document:
    """Document class for handling the document file"""

    def __init__(self, file_path: str):
        """Initialize the document object with the file path"""
        self.file = Path(file_path)

    def read_presentation(self) -> str:
        """Read the presentation from the document file"""
        with self.file.open("r", encoding="utf-8") as file:
            return file.read()

    def get_speaker_notes(self) -> str:
        """Read the speaker notes from the document file"""
        with self.file.open("r", encoding="utf-8") as stream:
            return stream.read()
