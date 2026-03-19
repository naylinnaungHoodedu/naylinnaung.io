import os
import re

directory = r"c:/Users/user/Downloads/Alam/nay_linn_aung_profile"
pattern = r'<link rel="icon" href="assets/images/favicon\.png" type="image/x-icon">'
replacement = r'<link rel="icon" href="assets/images/favicon.png?v=2" type="image/x-icon">'

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        if replacement not in content: # Avoid double patching
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {filename}")
                count += 1
            else:
                print(f"No match in {filename}")
        else:
             print(f"Already updated {filename}")

print(f"Total files updated: {count}")
