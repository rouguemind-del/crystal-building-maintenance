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

# Standard Additional Services content
STANDARD_ADDITIONAL_SERVICES = """
                <h3>Additional Services Offered To Existing Customers</h3>
                <ul>
                    <li>Day Porter Service</li>
                    <li>Special Cleaning Projects</li>
                    <li>Window Cleaning</li>
                    <li>Provide Customer Use Supplies (Paper Products, Hand Soap, Trash Liners)</li>
                </ul>"""

print("Starting fixes for all remaining issues...")

# 1. Fix Restaurant/Country Club page
print("\n1. Fixing Restaurant/Country Club page...")
content = read_file('restaurant-country-club-cleaning.html')

# Remove "Degrease ovens, stoves, grills and broilers"
content = re.sub(r'<li>\s*Degrease ovens, stoves, grills and broilers\s*</li>', '', content)

# Fix the Country Club Additional Services section - replace wrong content
# Find and replace the incorrect Additional Services section for Country Club
pattern = r'(<h3>Additional Services Offered To Existing Customers</h3>\s*<ul>.*?</ul>)'
replacement = STANDARD_ADDITIONAL_SERVICES

# Look for the section after "Quality Assurance Program" and replace it
content = re.sub(
    r'<h3>Additional Services Offered To Existing Customers</h3>\s*<ul>.*?</ul>',
    STANDARD_ADDITIONAL_SERVICES,
    content,
    flags=re.DOTALL
)

write_file('restaurant-country-club-cleaning.html', content)
print("✅ Restaurant/Country Club page fixed")

# 2. Fix Schools page - change title
print("\n2. Fixing Schools page...")
content = read_file('schools-cleaning.html')
content = re.sub(
    r'<title>School Janitorial Cleaning',
    '<title>Private School Janitorial Cleaning',
    content
)
content = re.sub(
    r'<h1>School Janitorial Cleaning',
    '<h1>Private School Janitorial Cleaning',
    content
)
content = re.sub(
    r'School Janitorial Cleaning Services',
    'Private School Janitorial Cleaning Services',
    content
)
write_file('schools-cleaning.html', content)
print("✅ Schools page fixed")

# 3. Fix Medical page
print("\n3. Fixing Medical page...")
content = read_file('medical-facility-cleaning.html')

# Fix mislabeled section
content = re.sub(
    r'<h3>Kitchen and Break Room Areas</h3>(\s*<ul>.*?Day Porter Service.*?</ul>)',
    STANDARD_ADDITIONAL_SERVICES,
    content,
    flags=re.DOTALL
)

# Remove Day Porter from Kitchen section if it's there
content = re.sub(
    r'<li>\s*Day Porter Service\s*</li>',
    '',
    content
)

write_file('medical-facility-cleaning.html', content)
print("✅ Medical page fixed")

# 4. Fix Retail page
print("\n4. Fixing Retail page...")
content = read_file('retail-stores-cleaning.html')

# Fix mislabeled section
content = re.sub(
    r'<h3>Kitchen and Break Room Areas</h3>',
    '<h3>Additional Services Offered To Existing Customers</h3>',
    content
)

write_file('retail-stores-cleaning.html', content)
print("✅ Retail page fixed")

# 5. Fix Theaters page
print("\n5. Fixing Theaters page...")
content = read_file('theaters-cleaning.html')

# First, fix the "Work To Be Performed On a Rotating Basis" section
# It should have the proper rotating content, not the additional services
rotating_content = """
                <h3>Work To Be Performed On a Rotating Basis</h3>
                <ul>
                    <li>High dusting of ceiling areas, lights, vents</li>
                    <li>Deep cleaning of theater seating</li>
                    <li>Carpet extraction and stain removal</li>
                    <li>Floor stripping and refinishing</li>
                    <li>Detailed cleaning of projection areas</li>
                </ul>"""

# Replace the incorrect rotating basis section
content = re.sub(
    r'<h3>Work To Be Performed On a Rotating Basis</h3>\s*<ul>.*?</ul>',
    rotating_content,
    content,
    flags=re.DOTALL
)

# Add the missing Additional Services section if it doesn't exist
if 'Additional Services Offered To Existing Customers' not in content:
    # Add it before the closing div of the service content
    content = re.sub(
        r'(</div>\s*</div>\s*</section>\s*<!-- CTA Section -->)',
        STANDARD_ADDITIONAL_SERVICES + r'\n            \1',
        content
    )

write_file('theaters-cleaning.html', content)
print("✅ Theaters page fixed")

# 6. Fix Religious Organizations page
print("\n6. Fixing Religious Organizations page...")
content = read_file('religious-organizations-cleaning.html')

# Add both missing sections
rotating_content_religious = """
                <h3>Work To Be Performed On a Rotating Basis</h3>
                <ul>
                    <li>High dusting of ceiling areas and fixtures</li>
                    <li>Deep cleaning of pews and seating</li>
                    <li>Floor stripping and refinishing</li>
                    <li>Window cleaning (interior and exterior)</li>
                    <li>Detailed cleaning of altar and sacred areas</li>
                </ul>"""

# Add both sections before the Quality Assurance section
if 'Work To Be Performed On a Rotating Basis' not in content:
    # Find the Quality Assurance section and insert before it
    content = re.sub(
        r'(<h3>Quality Assurance Program</h3>)',
        rotating_content_religious + '\n\n' + STANDARD_ADDITIONAL_SERVICES + '\n\n' + r'\1',
        content
    )

write_file('religious-organizations-cleaning.html', content)
print("✅ Religious Organizations page fixed")

# 7. Fix Health Clubs page
print("\n7. Fixing Health Clubs page...")
content = read_file('health-clubs-cleaning.html')

# Add missing Additional Services section
if 'Additional Services Offered To Existing Customers' not in content:
    # Add it before the closing div of the service content
    content = re.sub(
        r'(</div>\s*</div>\s*</section>\s*<!-- CTA Section -->)',
        STANDARD_ADDITIONAL_SERVICES + r'\n            \1',
        content
    )

write_file('health-clubs-cleaning.html', content)
print("✅ Health Clubs page fixed")

print("\n✅ All fixes completed successfully!")
print("\nSummary of changes:")
print("- Restaurant/Country Club: Removed 'Degrease ovens' and fixed Additional Services")
print("- Schools: Changed title to 'Private School Janitorial Cleaning'")
print("- Medical: Fixed mislabeled section and removed misplaced Day Porter")
print("- Retail: Fixed mislabeled 'Kitchen' section to 'Additional Services'")
print("- Theaters: Fixed rotating section content and added missing Additional Services")
print("- Religious Organizations: Added both missing sections")
print("- Health Clubs: Added missing Additional Services section")