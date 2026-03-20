import glob
import re

files = glob.glob('*.html')
count = 0
nav_pattern = re.compile(r'(<li><a href="projects\.html"(?: class="active")?>Projects</a></li>)')
replacement = r'\1\n                <li><a href="xai.html">Explainable AI</a></li>'

for f in files:
    if f == 'xai.html':
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    if 'xai.html' not in content:
        new_content = nav_pattern.sub(replacement, content)
        if new_content != content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            count += 1
            print(f"Updated {f}")
print(f"Total files updated: {count}")
