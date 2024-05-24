"""
This is the paragraph splitter/formatter to format 
Project Gutenberg-like works.
"""

from secrets_list import files
import json
import csv

list_of_text = []
fields = ['output']

def format_text(file_num, file):
    f = open(file, 'r', encoding='utf-8')
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

with open("formatting.json", "w", encoding='utf-8') as outfile:
    outfile.write(list_of_text_json)

with open("formatting.csv", 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(list_of_text)