import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the redundant `mb-5` from the main row
    content = content.replace('<div class="row g-4 mb-5">', '<div class="row g-4 justify-content-between">')
    
    # Change col-lg-8 to col-lg-7 to create space between logo and links
    content = content.replace('<div class="col-lg-8 col-md-12">', '<div class="col-lg-7 col-md-12">')
    
    # Remove pt-4 border-top from footer-bottom because style.css already does it perfectly
    content = content.replace('<div class="footer-bottom d-flex flex-column flex-md-row justify-content-between align-items-center pt-4 border-top">', '<div class="footer-bottom d-flex flex-column flex-md-row justify-content-between align-items-center">')
    
    # Also adjust the Contact text colors to match the rest of the site links?
    # Old quote section used default span color and primary color for links?
    # Let's remove `fw-bold text-dark` so it uses the natural footer link styles or general text styles.
    content = content.replace('class="text-dark fw-bold text-decoration-none"', 'class="text-decoration-none" style="color: #131313;"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Spacing fixed.")
