from difflib import Differ, SequenceMatcher

with open ("https___code.jquery.com_jquery-1.11.3.js") as f:
    file1_lines = f.readlines()
with open ("jquery-1.11.3.js") as f:
    file2_lines = f.readlines()

sm=SequenceMatcher(a=file1_lines, b=file2_lines);
print(sm.ratio())