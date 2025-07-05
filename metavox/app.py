"""Entry point for the Metavox application"""

import sys
import logging as log
import metavox.presentation as pt


log.basicConfig(level=log.INFO)


def main():
    """Main function to run the Metavox application"""
    log.info("Starting Metavox application...")

    if len(sys.argv) < 2:
        log.error("Usage: python app.py <presentation_file>")
        sys.exit(1)

    # read presentation file
    presentation = pt.read_presentation(sys.argv[1])
    for i, _ in enumerate(presentation.slides):
        notes = pt.get_speaker_notes(presentation, i)
        log.info(f"Speaker Notes: {i} {notes}")


if __name__ == "__main__":
    main()
