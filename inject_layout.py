import os
import glob
import re

html_files = glob.glob('*.html')
# We exclude the files we literally just built with the new layout
core_files = ['index.html', 'about.html', 'contact.html', 'experience.html', 'projects.html', 'skills.html']
files_to_update = [f for f in html_files if f not in core_files]

new_sidebar = """<body>
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
        <div class="brand">
            <a href="index.html">
                <h1>NAY LINN AUNG</h1>
            </a>
        </div>

        <nav>
            <span class="section-label">Work</span>
            <ul class="nav-links">
                <li><a href="experience.html">Experience</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="skills.html">Skills & Certs</a></li>
            </ul>

            <span class="section-label" style="margin-top: 2rem;">Info</span>
            <ul class="nav-links">
                <li><a href="about.html">About</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li><a href="blog.html" class="active">Blog</a></li>
                <li><a href="assets/docs/Nay_Linn_Aung_Resume.pdf" target="_blank"><i class="fas fa-file-pdf"></i> Resume</a></li>
            </ul>
        </nav>

        <div class="social-links">
            <a href="https://linkedin.com/in/naylinnaung" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/naylinnaung" target="_blank"><i class="fab fa-github"></i></a>
            <a href="mailto:naylinnaung.234@gmail.com"><i class="fas fa-envelope"></i></a>
        </div>
    </aside>

    <!-- Main Content Area -->
    <main class="main-content">
        <div class="content-container">"""

for file in files_to_update:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We need to strip the old <header>...</header>
    content = re.sub(r'<header.*?</header>', '', content, flags=re.DOTALL)
    
    # We need to strip the old footer completely
    content = re.sub(r'<footer.*?</footer>', '', content, flags=re.DOTALL)
    
    # We replace the starting <body> with our new layout injected
    # Ensure we only replace the first occurrence or just replace '<body>' exactly. 
    # Current files have <body>
    content = content.replace('<body>', new_sidebar, 1)
    
    # We need to close the main-content wrapper before </body>
    content = content.replace('</body>', '\n        </div>\n    </main>\n</body>')
    
    # Optional: We could also re-link the fonts/css if they are slightly off, but the old ones were ok-ish.
    # Let's enforce Thiri Oo's CSS and Inter font
    if 'fonts.googleapis.com' not in content:
        head_inject = '''    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'''
        content = content.replace('</head>', f'{head_inject}\n</head>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(files_to_update)} files to use the new side-nav layout.")
