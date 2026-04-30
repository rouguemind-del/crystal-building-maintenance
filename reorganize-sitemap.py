#!/usr/bin/env python3
import re
import os
from pathlib import Path

# Change to script directory
os.chdir(Path(__file__).parent)

# Read the current sitemap
with open('sitemap.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the sections we need
hero_match = re.search(r'<!-- Hero Section -->.*?</section>', content, re.DOTALL)
services_match = re.search(r'<!-- Services Directory -->.*?</section>', content, re.DOTALL)
areas_match = re.search(r'<!-- Areas Directory -->.*?</section>', content, re.DOTALL)
contact_match = re.search(r'<!-- Contact Information -->.*?</section>', content, re.DOTALL)
footer_match = re.search(r'<!-- Footer -->.*?</html>', content, re.DOTALL)

if not all([hero_match, services_match, areas_match, footer_match]):
    print("ERROR: Could not find all sections")
    exit(1)

# Get the header and hero
header_end = content.find('<!-- Hero Section -->')
header = content[:header_end]
hero = hero_match.group()
areas = areas_match.group()
services = services_match.group()
footer = footer_match.group()

# Convert services from big cards to compact list
services_compact = """  <!-- Services List -->
  <section class="services-list-compact">
   <div class="container">
    <h2 id="services">Commercial Cleaning Services</h2>
    <div class="services-columns">
     <ul class="service-list">
      <li><a href="commercial-cleaning.html">Commercial Office Cleaning</a></li>
      <li><a href="medical-facility-cleaning.html">Medical Facility Cleaning</a></li>
      <li><a href="condo-hoa-cleaning.html">Condo HOA Porter Service</a></li>
      <li><a href="restaurant-country-club-cleaning.html">Country Club / Clubhouse</a></li>
      <li><a href="religious-organizations-cleaning.html">Religious Organizations</a></li>
      <li><a href="health-clubs-cleaning.html">Health Clubs</a></li>
     </ul>
     <ul class="service-list">
      <li><a href="municipal-government-cleaning.html">Municipal Governments</a></li>
      <li><a href="schools-cleaning.html">Private Schools</a></li>
      <li><a href="theaters-cleaning.html">Theaters</a></li>
      <li><a href="retail-stores-cleaning.html">Retail Stores</a></li>
      <li><a href="industrial-cleaning.html">Industrial Facilities</a></li>
      <li><a href="banks-cleaning.html">Banks & Financial</a></li>
     </ul>
    </div>
   </div>
  </section>"""

# Build the new sitemap with areas first
new_sitemap = header + hero + areas + services_compact + footer

# Save the reorganized sitemap
with open('sitemap.html', 'w', encoding='utf-8') as f:
    f.write(new_sitemap)

print("✅ Sitemap reorganized successfully!")
print("- Areas/Map section moved to TOP (after hero)")
print("- Services converted to compact list")
print("- Contact section removed (duplicate)")
print("- Focus is now on SERVICE AREAS as requested")