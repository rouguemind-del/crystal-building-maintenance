#!/usr/bin/env python3
"""
Fix final CBM website issues:
1. Footer typo on all pages
2. About page duplicate "Robert"
3. Reduce video display size
4. Add third YouTube video
"""

import re
import glob

def fix_footer_typo(content):
    """Fix footer typo: Licensed, Bonded Licensed & Insuredamp; Insured -> Licensed, Bonded & Insured"""
    # Fix the malformed HTML entity
    content = content.replace(
        "Licensed, Bonded Licensed &amp; Insuredamp; Insured",
        "Licensed, Bonded &amp; Insured"
    )
    return content

def fix_operations_duplicate(content):
    """Fix About page: Operations: Robert Robert Friedman -> Operations: Robert Friedman"""
    content = content.replace(
        "<p><strong>Operations: Robert</strong> Robert Friedman",
        "<p><strong>Operations:</strong> Robert Friedman"
    )
    return content

def add_third_video(content):
    """Add third YouTube video to the index.html video section"""
    # Only process if this is index.html and has the video section
    if '<div class="videos-grid">' in content and 'l0yhvbN5Ta8' in content:
        # Find the closing div of the videos-grid
        video_section = """     <div class="video-container">
      <iframe src="https://www.youtube.com/embed/l0yhvbN5Ta8" title="Crystal Building Maintenance - Equipment &amp; Standards">
      </iframe>
      <h3>
       Professional Equipment
      </h3>
      <p>
       Commercial-grade cleaning supplies and equipment for superior cleaning results in all environments.
      </p>
     </div>"""
        
        # Add the third video
        third_video = """
     <div class="video-container">
      <iframe src="https://www.youtube.com/embed/_OpwmAQzQOM" title="Crystal Building Maintenance - Service Excellence">
      </iframe>
      <h3>
       Service Excellence
      </h3>
      <p>
       Dedicated to maintaining the highest standards of cleanliness and customer satisfaction.
      </p>
     </div>"""
        
        # Insert the third video after the second one
        content = content.replace(
            video_section + '\n    </div>',
            video_section + third_video + '\n    </div>'
        )
    
    return content

def update_video_css(css_content):
    """Update CSS to reduce video display size"""
    # Update the video-grid max-width
    css_content = re.sub(
        r'\.video-grid\s*{([^}]+)max-width:\s*900px;',
        r'.video-grid {1max-width: 1200px;',
        css_content,
        flags=re.DOTALL
    )
    
    # Update grid template columns for smaller videos
    css_content = re.sub(
        r'(\.video-grid\s*{[^}]*grid-template-columns:\s*)repeat\(auto-fit,\s*minmax\(400px,\s*1fr\)\)',
        r'1repeat(auto-fit, minmax(300px, 1fr))',
        css_content,
        flags=re.DOTALL
    )
    
    # Add specific video sizing
    if '.video-container {' in css_content:
        # Add max-width to video containers
        css_content = re.sub(
            r'(\.video-container\s*{)',
            r'1\n    max-width: 400px;\n    margin: 0 auto;',
            css_content
        )
    
    return css_content

def update_videos_grid_css(css_content):
    """Add videos-grid specific styling"""
    # Check if videos-grid class exists, if not add it
    if '.videos-grid' not in css_content:
        # Add after .video-grid
        video_grid_css = """
/* Videos Grid - 3 column layout */
.videos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin: 3rem auto;
    max-width: 1200px;
}

.videos-grid .video-container {
    max-width: 100%;
}

@media (max-width: 768px) {
    .videos-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
}
"""
        # Insert after .video-grid section
        css_content = re.sub(
            r'(\.video-container:hover\s*{[^}]+})',
            r'\g<1>' + video_grid_css,
            css_content,
            flags=re.DOTALL
        )
    
    return css_content

def main():
    # Process all HTML files
    html_files = glob.glob('*.html')
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes
        content = fix_footer_typo(content)
        
        # Only fix operations duplicate in about.html
        if 'about.html' in filepath:
            content = fix_operations_duplicate(content)
        
        # Only add third video to index.html
        if 'index.html' in filepath and 'index-' not in filepath:
            content = add_third_video(content)
        
        # Write back if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {filepath}")
    
    # Update CSS for video sizing
    css_file = 'styles.css'
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    original_css = css_content
    css_content = update_video_css(css_content)
    css_content = update_videos_grid_css(css_content)
    
    if css_content != original_css:
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css_content)
        print(f"Updated CSS: {css_file}")
    
    print("\nAll fixes completed!")
    print("- Footer typo fixed on all pages")
    print("- About page 'Robert Robert' duplicate fixed")
    print("- Video display size reduced")
    print("- Third YouTube video added to index.html")

if __name__ == "__main__":
    main()