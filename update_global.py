import os
import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update phone number
    content = content.replace('(301) 676-4780', '(301) 676-6780')

    # 2. Update footer
    content = content.replace('© <span id="year"></span> Nay Linn Aung. Designed for Professional Excellence.', 
                              '© 2026 Nay Linn Aung. All rights reserved.')
    # Also handle if it was already replaced or slightly different format
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Global replacements completed!")
