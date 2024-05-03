from xml.etree import ElementTree as ET
import os

def txt_to_html(txt_file, html_file):
  """
  Converts a text file with header and paragraph to an HTML file.
  Make necessary changes for multiple news articles. This script is
  only for one news article.

  Args:
      txt_file (str): Path to the text file.
      html_file (str): Path to the output HTML file.
  """
  # Create root element for HTML
  root = ET.Element("html")

  # Create head and body elements
  ## SubElement() is used to create new elements as children of existing elements in an xml Tree
  head = ET.SubElement(root, "head")
  title = ET.SubElement(head, "title")
  title.text = "My News Aggregation Site"
  body = ET.SubElement(root, "body")

  # Loop through each text file
  for txt_file in txt_files:
      # Read text file content
      with open(txt_file, 'r') as f:
          content = f.readlines()

      # Extract header and paragraph
      header = content[0].strip()
      paragraph = "".join(content[1:]).strip()

      # Create header and paragraph elements in body
      ## SubElement() is used to create new elements as children of existing elements in an xml Tree
      h1 = ET.SubElement(body, "h1")
      h1.text = header
      p = ET.SubElement(body, "p")
      p.text = paragraph

  # Write HTML tree to file
  with open(html_file, 'wb') as f:
      tree = ET.ElementTree(root)
      tree.write(f, encoding='utf-8')


# Directory containing the text files
txt_files_dir = "../DataX/generated"
# List all the text files in the directory
txt_files = [os.path.join(txt_files_dir, file) for file in os.listdir(txt_files_dir) if file.endswith('.txt')]

# Output HTML file
html_file = "display.html"

# Convert text files to HTML
txt_to_html(txt_files, html_file)

print(f"Converted text files to HTML file '{html_file}'.")
