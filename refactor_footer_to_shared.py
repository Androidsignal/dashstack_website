import glob
import re
import os

replacement_html = """  <!-- Footer Placeholder -->
  <div id="footer-placeholder"></div>
  <script src="./js/footer-loader.js"></script>"""

html_files = glob.glob('*.html')
footer_regex = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if it already has the placeholder so we don't duplicate
    if 'id="footer-placeholder"' in content:
        print(f"Skipping {f}, already refactored.")
        continue

    new_content = footer_regex.sub(replacement_html, content)
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Refactored footer in {f}")
    else:
        print(f"No footer tag found in {f}")

print("Footer refactor complete.")
