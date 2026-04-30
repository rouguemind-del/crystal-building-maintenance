#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Change to the script's directory
os.chdir(Path(__file__).parent)

def read_file(filename):
    """Read file with proper encoding handling"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='latin-1') as f:
            return f.read()

def write_file(filename, content):
    """Write file with proper encoding handling"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except UnicodeEncodeError:
        with open(filename, 'w', encoding='latin-1') as f:
            f.write(content)

# Get all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Fixing About nav link and removing Watch Our Team section...")
print(f"Processing {len(html_files)} HTML files...")

files_updated = 0

for filename in html_files:
    content = read_file(filename)
    original_content = content
    
    # 1. Fix About nav link - change #about or index.html#about to about.html
    content = re.sub(
        r'href="(?:index\.html)?#about"',
        'href="about.html"',
        content
    )
    
    # 2. Remove "Watch Our Team" title and subtitle from the video section
    # Remove the h2 "Watch Our Team" 
    content = re.sub(
        r'<h2[^>]*>\s*Watch Our Team\s*</h2>',
        '',
        content
    )
    
    # Remove the subtitle "See the quality of our work in action."
    content = re.sub(
        r'<p[^>]*>\s*See the quality of our work in action\.\s*</p>',
        '',
        content
    )
    
    # Also remove if they're in a different format
    content = re.sub(
        r'Watch Our Team',
        '',
        content
    )
    
    content = re.sub(
        r'See the quality of our work in action\.?',
        '',
        content
    )
    
    if content != original_content:
        write_file(filename, content)
        files_updated += 1
        print(f"✅ Updated: {filename}")

print(f"\n✅ Fixed {files_updated} files!")
print("- About nav link now points to about.html")
print("- Removed 'Watch Our Team' title and subtitle")