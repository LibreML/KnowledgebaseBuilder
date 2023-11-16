"""Code for the Custom Vector Graphic GPT that generates a Markdown image from an SVG string."""
import base64
import sys


def svg_to_markdown(svg_string, image_title):
    """A simple function to create Render-able Markdown from an SVG string."""
    encoded = base64.b64encode(svg_string.encode("utf-8")).decode("utf-8")
    return f"![{image_title}](data:image/svg+xml;base64,{encoded})"


stri_example = """<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
  <text x="50" y="55" font-size="9" text-anchor="middle" fill="black">Hello</text>
</svg>
"""

# Use this script with the arguments "": Name, and "": SVG String
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 svg_str_to_markdown.py <name> <svg_string_in_quotes>")
        sys.exit(1)
    print(svg_to_markdown(sys.argv[2], sys.argv[1]))
