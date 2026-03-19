import os
import glob
import re

html_files = glob.glob('*.html')
primary_files = ['index.html', 'about.html', 'blog.html']
secondary_files = [f for f in html_files if f not in primary_files]

nav_replacement_main = r'''                    <li><a href="index.html#skills">Skills</a></li>
                    <li><a href="index.html#contact">Contact</a></li>
                    <li><a href="blog.html">Blog</a></li>
                    <li><a href="assets/docs/Nay_Linn_Aung_Resume.pdf" target="_blank" class="download-btn"><i class="fas fa-file-pdf"></i> Resume</a></li>'''

nav_replacement_mobile = r'''                <li><a href="index.html#skills">Skills</a></li>
                <li><a href="index.html#contact">Contact</a></li>
                <li><a href="blog.html">Blog</a></li>
                <li><a href="assets/docs/Nay_Linn_Aung_Resume.pdf" target="_blank"><i class="fas fa-file-pdf"></i> Resume</a></li>'''

for file in secondary_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to target the block of 3 lines and replace it with 4.
    # We will use regex for a slightly more robust replacement since spacing might differ slightly, but simple string replacement is safer if exact.
    
    # Target 1 (Desktop nav):
    target_main = '''                    <li><a href="index.html#skills">Skills</a></li>
                    <li><a href="index.html#contact">Contact</a></li>
                    <li><a href="blog.html">Blog</a></li>'''
                    
    content = content.replace(target_main, nav_replacement_main)

    # Target 2 (Mobile nav):
    target_mobile = '''                <li><a href="index.html#skills">Skills</a></li>
                <li><a href="index.html#contact">Contact</a></li>
                <li><a href="blog.html">Blog</a></li>'''
                
    content = content.replace(target_mobile, nav_replacement_mobile)
    
    # Also fix meta tags if needed for these files
    if '<meta property="og:title"' not in content:
        # Just simple inject before title
        og_tags = f'''    <meta property="og:title" content="Nay Linn Aung | Senior Automation & Robotics Engineer">
    <meta property="og:description" content="Insights on Industrial Automation, AI, and SCADA by Nay Linn Aung">
    <meta property="og:image" content="https://naylinnaung.io/assets/images/NLA_Profile_Photo.jpg">
    <title>'''
        content = content.replace('<title>', og_tags)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print(f"Updated navigations for {len(secondary_files)} secondary files.")
