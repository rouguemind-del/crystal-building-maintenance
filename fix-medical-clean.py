#!/usr/bin/env python3
import re

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='latin-1') as f:
            return f.read()

def write_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
    except UnicodeEncodeError:
        with open(filename, 'w', encoding='latin-1') as f:
            f.write(content)

import os
from pathlib import Path

# Change to the script's directory
os.chdir(Path(__file__).parent)

# Read the medical file
content = read_file('medical-facility-cleaning.html')

# Find all Additional Services sections
pattern = r'<h3>Additional Services Offered To Existing Customers</h3>\s*<ul>.*?</ul>'
sections = re.findall(pattern, content, flags=re.DOTALL)

print(f"Found {len(sections)} Additional Services sections")

if len(sections) >= 2:
    # Remove ALL Additional Services sections first
    for section in sections:
        content = content.replace(section, '', 1)
    
    # Now add back ONE correct section with all 4 items
    correct_section = """<h3>Additional Services Offered To Existing Customers</h3>
                <ul>
                    <li>Day Porter Service</li>
                    <li>Special Cleaning Projects</li>
                    <li>Window Cleaning</li>
                    <li>Provide Customer Use Supplies (Paper Products, Hand Soap, Trash Liners)</li>
                </ul>"""
    
    # Find where to insert it (before Quality Assurance section)
    insertion_point = content.find('<h3>Quality Assurance Program</h3>')
    if insertion_point != -1:
        # Insert before Quality Assurance
        content = content[:insertion_point] + correct_section + '\n                \n                ' + content[insertion_point:]
    
    print("✅ Fixed: Removed duplicates and added one correct section with all 4 items")
    
    # Clean up any multiple blank lines
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    write_file('medical-facility-cleaning.html', content)
    print("✅ Medical page fixed and saved")
else:
    print("⚠️ Unexpected number of sections found")