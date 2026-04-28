#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Change to the script's directory
os.chdir(Path(__file__).parent)

# Get all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

print(f"Found {len(html_files)} HTML files to update")

for filename in html_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Try with latin-1 encoding if utf-8 fails
        with open(filename, 'r', encoding='latin-1') as f:
            content = f.read()
    
    original_content = content
    
    # 1. Make "Request a Free Quote" button green
    # Find and update the button styling to use green color
    content = re.sub(
        r'(<a[^>]*href="[^"]*request-quote[^"]*"[^>]*class="[^"]*)(">Request a Free Quote)',
        r'\1" style="background-color: #28a745; border-color: #28a745; color: white;\2',
        content,
        flags=re.IGNORECASE
    )
    
    # Also update any inline button styles
    content = re.sub(
        r'(Request a Free Quote</a>)',
        lambda m: m.group(0) if 'background-color: #28a745' in content[max(0, m.start()-200):m.start()] else m.group(0).replace('</a>', '</a>').replace('Request a Free Quote</a>', 'Request a Free Quote</a>'),
        content
    )
    
    # 2. Update contact/header section - Sales and Operations
    # Update Sales line
    content = re.sub(
        r'Sales \(New Customers\):\s*[^<\n]*',
        'Sales (New Customers): Randy',
        content
    )
    
    # Update Operations line
    content = re.sub(
        r'Operations:\s*[^<\n]*',
        'Operations: Robert',
        content
    )
    
    # 3. Remove the 3 services from "Additional Services Offered To Existing Customers"
    services_to_remove = [
        'Strip And Wax Tile Floors',
        'Machine Clean Hard Floors',
        'Carpet Cleaning Service'
    ]
    
    for service in services_to_remove:
        # Remove as list items
        content = re.sub(
            f'<li>\\s*{re.escape(service)}\\s*</li>',
            '',
            content,
            flags=re.IGNORECASE
        )
        
        # Remove from any comma-separated lists
        content = re.sub(
            f',\\s*{re.escape(service)}',
            '',
            content,
            flags=re.IGNORECASE
        )
        content = re.sub(
            f'{re.escape(service)}\\s*,',
            '',
            content,
            flags=re.IGNORECASE
        )
    
    # Clean up any empty ul tags or double line breaks
    content = re.sub(r'<ul>\s*</ul>', '', content)
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    if content != original_content:
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
        except UnicodeEncodeError:
            # Try with latin-1 encoding if utf-8 fails
            with open(filename, 'w', encoding='latin-1') as f:
                f.write(content)
        print(f"✅ Updated: {filename}")
    else:
        print(f"⏭️  No changes needed: {filename}")

print("\n✅ All updates completed!")