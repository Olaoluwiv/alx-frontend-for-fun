#!/usr/bin/python3
import sys
import os

def markdown_to_html(input_file, output_file):
    # Ensure that there are exactly 2 arguments provided
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # No further processing is required as per the given requirements
    sys.exit(0)

if __name__ == "__main__":
    # Capture the command line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else ""
    output_file = sys.argv[2] if len(sys.argv) > 2 else ""

    # Run the conversion function
    markdown_to_html(input_file, output_file)
