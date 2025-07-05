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

    
    pt.read_presentation("dummy_presentation.pptx")


if __name__ == "__main__":
    main()
