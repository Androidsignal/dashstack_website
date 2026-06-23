import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove contact-info from the left column
    # We'll extract it so we can re-use it (or just hardcode the new one)
    contact_info_pattern = re.compile(r'\s*<div class="contact-info">.*?</div>\s*(?=</div>\s*<!-- Center Columns)', re.DOTALL)
    
    new_contact_col = """          <div class="col-md-4 col-sm-12 mb-4">
            <h5 class="mb-4">Contact</h5>
            <div class="contact-info">
              <div class="mb-3">
                <span class="d-block text-muted">Drop Us An Email</span>
                <a href="mailto:team@dashstack.tech" class="text-dark fw-bold text-decoration-none">team@dashstack.tech</a>
              </div>
              <div>
                <span class="d-block text-muted">Call Our Project Experts</span>
                <a href="tel:+918153916802" class="text-dark fw-bold text-decoration-none">(+91) 8153 9168 02</a>
              </div>
            </div>
          </div>"""

    # 2. Find and replace the reviews column with the new contact column
    reviews_col_pattern = re.compile(r'<div class="col-md-4 col-sm-12 mb-4">\s*<h5 class="mb-4">Reviews</h5>.*?</div>\s*</div>\s*</div>', re.DOTALL)
    
    # Let's be careful with the div closing tags.
    # The reviews column is the last div inside <div class="row"> inside <!-- Center Columns -->
    # It ends with:
    #           </div>
    #         </div>
    #       </div>
    # Let's do exact string replacement if possible, or targeted regex.
    
    # Let's just do a clean replacement of the whole row section if needed, or targeted replacements.
    
    # First, strip contact-info from the left column
    new_content = re.sub(r'\s*<div class="contact-info">.*?</div>\s*(?=</div>\s*<!-- Center Columns: Sitemap Links -->)', '\n      ', content, flags=re.DOTALL)
    
    # Then replace the reviews column
    # Reviews column starts with `<div class="col-md-4 col-sm-12 mb-4">\s*<h5 class="mb-4">Reviews</h5>`
    # and we want to replace that whole div.
    new_content = re.sub(r'<div class="col-md-4 col-sm-12 mb-4">\s*<h5 class="mb-4">Reviews</h5>.*?</div>\s*</div>\s*</div>\s*</div>', new_contact_col + '\n        </div>\n      </div>', new_content, flags=re.DOTALL)

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("Updates applied.")
