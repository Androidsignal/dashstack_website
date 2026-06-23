import glob
import re

new_footer = """<footer class="footer">
  <div class="container">
    <div class="row g-4 mb-5">
      <!-- Left Column: Logo & Tagline -->
      <div class="col-lg-4 col-md-12">
        <img src="./images/h_logo.png" alt="DashStack Footer Logo" class="footer-logo mb-3" style="max-width: 200px;" />
        <p class="mb-4">
          Powering Digital Journeys from<br />
          Startups to Enterprises.
        </p>
        <div class="contact-info">
          <div class="mb-2">
            <span class="d-block text-muted">Drop Us An Email</span>
            <a href="mailto:team@dashstack.tech" class="text-dark fw-bold text-decoration-none">team@dashstack.tech</a>
          </div>
          <div>
            <span class="d-block text-muted">Call Our Project Experts</span>
            <a href="tel:+918153916802" class="text-dark fw-bold text-decoration-none">(+91) 8153 9168 02</a>
          </div>
        </div>
      </div>

      <!-- Center Columns: Sitemap Links -->
      <div class="col-lg-8 col-md-12">
        <div class="row">
          <div class="col-md-4 col-sm-6 mb-4">
            <h5 class="mb-4">Company</h5>
            <ul>
              <li><a href="/index.html#about">Who we are</a></li>
              <li><a href="/index.html#services">Our services</a></li>
              <li><a href="/index.html#testimonial">Our clients</a></li>
              <li><a href="/contact.html">Contact us</a></li>
            </ul>
          </div>
          <div class="col-md-4 col-sm-6 mb-4">
            <h5 class="mb-4">Services</h5>
            <ul>
              <li><a href="/index.html#services">Flutter App Development</a></li>
              <li><a href="/index.html#services">IoT & BLE Apps</a></li>
              <li><a href="/index.html#services">Real-Time Video Apps</a></li>
              <li><a href="/index.html#services">AI-Powered Apps</a></li>
            </ul>
          </div>
          <div class="col-md-4 col-sm-12 mb-4">
            <h5 class="mb-4">Reviews</h5>
            <div class="clutch-widget-container">
              <script type="text/javascript" src="https://widget.clutch.co/static/js/widget.js"></script>
              <div class="clutch-widget" data-url="https://widget.clutch.co" data-widget-type="1" data-height="40" data-nofollow="false" data-expandifr="true" data-scale="100" data-clutchcompany-id="2555160"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Bottom Row: Copyright & Socials -->
    <div class="footer-bottom d-flex flex-column flex-md-row justify-content-between align-items-center pt-4 border-top">
      <p class="mb-md-0" aria-label="Mobile App Development Company">
        © 2026 DashStack Infotech – Flutter App Development Company. All rights reserved.
      </p>
      <div class="social-icons">
        <a class="me-2" href="https://in.linkedin.com/company/dashstack-infotech" target="_blank" rel="noopener">
          <img src="./images/linkedin_icon.avif" alt="LinkedIn" />
        </a>
        <a class="me-2" href="https://pub.dev/publishers/dashstack.tech/packages" target="_blank" rel="noopener">
          <img src="./images/flutter_icon.avif" alt="Flutter Open-Source Packages" />
        </a>
        <a class="me-2" href="https://share.google/jNeEXJylERyU6zyFs" target="_blank" rel="noopener">
          <img src="./images/google_icon.avif" alt="Google" />
        </a>
        <a href="https://www.instagram.com/dashstack_infotech" target="_blank" rel="noopener">
          <img src="./images/instagram_icon.avif" alt="Instagram" />
        </a>
      </div>
    </div>
  </div>
</footer>"""

html_files = glob.glob('*.html')
footer_regex = re.compile(r'<footer class="footer">.*?</footer>', re.DOTALL)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content = footer_regex.sub(new_footer, content)
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)

print("Replacement complete.")
