"""
This is the paragraph splitter/formatter to format 
Project Gutenberg-like works.
"""

from secrets_list import files
import json

list_of_text = []

def format_text(file_num, file):
    f = open(file, 'r', encoding='utf8')
    paragraph = []
    for idx, sentence in enumerate(f):
        line = sentence.strip()
        if (idx % 1000 == 0):
            print(f"FILE {file_num}, LINE {idx}")
        if len(line) > 0:
            paragraph.append(line)
        elif len(paragraph) > 1:
            paragraph_text = ' '.join(paragraph)
            list_of_text.append({
                "output": paragraph_text
            })
            paragraph.clear()
        else:
            paragraph.clear()
    if len(paragraph) > 0:
        paragraph_text = ' '.join(paragraph)
        list_of_text.append({
            "output": paragraph_text
        })

for file_num, file in enumerate(files):
    format_text(file_num, f"./texts/{file}")

print(f"LIST LENGTH: {len(list_of_text)}")

list_of_text_json = json.dumps(list_of_text)

with open("formatting.json", "w") as outfile:
    outfile.write(list_of_text_json)
