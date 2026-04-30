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

print("Fixing final 3 issues...")

# 1. Fix Schools page - H1 heading
print("\n1. Fixing Schools page H1 heading...")
content = read_file('schools-cleaning.html')

# Fix the H1 heading on the page
content = re.sub(
    r'<h1>School Janitorial Cleaning',
    '<h1>Private School Janitorial Cleaning',
    content
)

# Also check for any other instances
content = re.sub(
    r'>School Janitorial Cleaning<',
    '>Private School Janitorial Cleaning<',
    content
)

write_file('schools-cleaning.html', content)
print("✅ Schools page H1 heading fixed")

# 2. Fix Medical page - remove duplicate Additional Services section
print("\n2. Fixing Medical page duplicate sections...")
content = read_file('medical-facility-cleaning.html')

# Count how many "Additional Services" sections exist
count = content.count('Additional Services Offered To Existing Customers')
print(f"   Found {count} 'Additional Services' sections")

# Find and remove the incomplete one (missing Day Porter)
# First, let's identify the pattern of the incomplete section
# It should have the heading but be missing Day Porter Service

# Strategy: Find all Additional Services sections and keep only the complete one
sections = re.findall(
    r'<h3>Additional Services Offered To Existing Customers</h3>\s*<ul>.*?</ul>',
    content,
    flags=re.DOTALL
)

if len(sections) > 1:
    # Find the complete section (one with Day Porter)
    complete_section = None
    for section in sections:
        if 'Day Porter Service' in section:
            complete_section = section
            break
    
    if complete_section:
        # Remove all sections first
        for section in sections:
            content = content.replace(section, '[PLACEHOLDER]', 1)
        
        # Put back only the complete section at the first placeholder
        content = content.replace('[PLACEHOLDER]', complete_section, 1)
        # Remove any remaining placeholders
        content = content.replace('[PLACEHOLDER]', '')
        
print("✅ Medical page duplicate section removed")

write_file('medical-facility-cleaning.html', content)

# 3. Fix Retail page - fix mislabeled Kitchen content
print("\n3. Fixing Retail page mislabeled section...")
content = read_file('retail-stores-cleaning.html')

# Find the mislabeled section with kitchen content
# Replace the heading for the section that has kitchen content
pattern = r'<h3>Additional Services Offered To Existing Customers</h3>(\s*<ul>.*?counter tops.*?</ul>)'
replacement = r'<h3>Kitchen and Break Room Areas</h3>\1'

content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Alternative: if the above doesn't work, try a more specific pattern
if 'counter tops' in content and 'Additional Services Offered To Existing Customers' in content:
    # Find the section with kitchen content and fix its heading
    content = re.sub(
        r'<h3>Additional Services Offered To Existing Customers</h3>(\s*<ul>\s*<li>Clean and sanitize counter tops, tables, sinks, and chairs</li>.*?</ul>)',
        r'<h3>Kitchen and Break Room Areas</h3>\1',
        content,
        flags=re.DOTALL
    )

write_file('retail-stores-cleaning.html', content)
print("✅ Retail page mislabeled section fixed")

print("\n✅ All 3 final issues fixed!")
print("\nSummary:")
print("- Schools: Fixed H1 heading to 'Private School Janitorial Cleaning'")
print("- Medical: Removed duplicate/incomplete Additional Services section")
print("- Retail: Renamed mislabeled section from 'Additional Services' to 'Kitchen and Break Room Areas'")