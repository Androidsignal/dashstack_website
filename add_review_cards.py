import glob
import re

html_files = glob.glob('*.html')

old_reviews_col = """          <div class="col-md-4 col-sm-12 mb-4">
            <h5 class="mb-4">Reviews</h5>
            <div class="clutch-widget-container">
              <script type="text/javascript" src="https://widget.clutch.co/static/js/widget.js"></script>
              <div class="clutch-widget" data-url="https://widget.clutch.co" data-widget-type="1" data-height="40" data-nofollow="false" data-expandifr="true" data-scale="100" data-clutchcompany-id="2555160"></div>
            </div>
          </div>"""

new_reviews_col = """          <div class="col-md-4 col-sm-12 mb-4">
            <h5 class="mb-4">Reviews</h5>
            <div class="d-flex flex-column gap-3">
              <div class="clutch-widget-container">
                <script type="text/javascript" src="https://widget.clutch.co/static/js/widget.js"></script>
                <div class="clutch-widget" data-url="https://widget.clutch.co" data-widget-type="1" data-height="40" data-nofollow="false" data-expandifr="true" data-scale="100" data-clutchcompany-id="2555160"></div>
              </div>
              
              <a href="#" class="review-card google-card" target="_blank" rel="noopener">
                <div class="d-flex align-items-center justify-content-between">
                  <div class="d-flex align-items-center gap-2">
                    <img src="./images/google_icon.avif" alt="Google" style="width: 20px;" />
                    <span class="fw-bold text-dark" style="font-size: 14px;">Google Reviews</span>
                  </div>
                  <div class="d-flex align-items-center">
                    <span class="fw-bold me-1 text-dark" style="font-size: 14px;">5.0</span>
                    <span class="text-warning" style="font-size: 14px;">★★★★★</span>
                  </div>
                </div>
              </a>

              <a href="#" class="review-card upwork-card" target="_blank" rel="noopener">
                <div class="d-flex align-items-center justify-content-between">
                  <div class="d-flex align-items-center gap-2">
                    <span class="fw-bold text-success" style="font-family: Arial, sans-serif; font-size: 16px;">Upwork</span>
                  </div>
                  <div class="d-flex align-items-center">
                    <span class="fw-bold me-1 text-dark" style="font-size: 14px;">5.0</span>
                    <span class="text-warning" style="font-size: 14px;">★★★★★</span>
                  </div>
                </div>
              </a>
            </div>
          </div>"""

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We can do an exact replacement
    new_content = content.replace(old_reviews_col, new_reviews_col)
    
    # Fallback to regex if exact replacement fails due to spacing
    if new_content == content:
        pattern = re.compile(r'<div class="col-md-4 col-sm-12 mb-4">\s*<h5 class="mb-4">Reviews</h5>\s*<div class="clutch-widget-container">.*?</div>\s*</div>', re.DOTALL)
        new_content = pattern.sub(new_reviews_col, content)
        
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("Replacement complete.")
