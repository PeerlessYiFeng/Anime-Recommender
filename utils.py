import re
import html

def clean_title(name):
    name = re.sub(r'\s+', ' ', name)  # Remove extra spaces
    return name.strip()

def fix_name_encoding(name):
    return html.unescape(name)
