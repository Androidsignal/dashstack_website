import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Change col-lg-4 for logo to col-lg-3
    content = content.replace('<div class="col-lg-4 col-md-12">', '<div class="col-lg-3 col-md-12 mb-4">')
    
    # 2. Remove the wrapper div `col-lg-7 col-md-12` and its inner `<div class="row">`
    # Also remove the closing tags for those two divs.
    # The structure to remove:
    #       <!-- Center Columns: Sitemap Links -->
    #       <div class="col-lg-7 col-md-12">
    #         <div class="row">
    content = content.replace('      <!-- Center Columns: Sitemap Links -->\n      <div class="col-lg-7 col-md-12">\n        <div class="row">\n', '')
    
    # Change inner columns to be col-lg-3
    content = content.replace('<div class="col-md-4 col-sm-6 mb-4">', '<div class="col-lg-3 col-md-4 col-sm-6 mb-4">')
    content = content.replace('<div class="col-md-4 col-sm-12 mb-4">', '<div class="col-lg-3 col-md-4 col-sm-12 mb-4">')
    
    # Remove the extra closing divs
    # At the end of the columns, we have:
    #         </div>
    #       </div>
    #     </div>
    #     <!-- Bottom Row: Copyright & Socials -->
    # We only need one `</div>` for the main row.
    content = content.replace('        </div>\n      </div>\n    </div>\n    \n    <!-- Bottom Row: Copyright & Socials -->', '    </div>\n    \n    <!-- Bottom Row: Copyright & Socials -->')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Columns equalized.")
