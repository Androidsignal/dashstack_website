import os
import glob
import re

html_files = glob.glob('*.html')

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove the newsletter block
    newsletter_pattern = re.compile(r'<div class="col-lg-6 col-md-12">\s*<h5>Subscribe newsletter</h5>.*?</div>\s*</div>', re.DOTALL)
    # Wait, the structure is:
    # <div class="col-lg-6 col-md-12">
    #   <h5>Subscribe newsletter</h5>
    #   ...
    # </div>
    # Let's replace precisely by looking for the <h5>Subscribe newsletter</h5> and its parent div.
    
    # Let's first make a copy of the content to see if we changed it
    new_content = content
    
    newsletter_block = re.search(r'<div class="col-lg-6 col-md-12">\s*<h5>Subscribe newsletter</h5>.*?</div>\s*(<div class="col-lg-2 col-md-4">)', new_content, re.DOTALL)
    if newsletter_block:
        new_content = new_content.replace(newsletter_block.group(0), newsletter_block.group(1))

    # 2. Update Services links
    services_pattern = r'<li><a href="#">Planning</a></li>\s*<li><a href="#">Research</a></li>\s*<li><a href="#">Consulting</a></li>\s*<li><a href="#">Analysis</a></li>'
    new_services = '''<li><a href="/index.html#services">Flutter App Development</a></li>
            <li><a href="/index.html#services">IoT & BLE Apps</a></li>
            <li><a href="/index.html#services">Real-Time Video Apps</a></li>
            <li><a href="/index.html#services">AI-Powered Apps</a></li>'''
    new_content = re.sub(services_pattern, new_services, new_content)
    
    # 3. Update Company links
    company_pattern = r'<li><a href="#about">Who we are</a></li>\s*<li><a href="#services">Our services</a></li>\s*<li><a href="#clients">Our clients</a></li>\s*<li><a href="#contact">Contact us</a></li>'
    new_company = '''<li><a href="/index.html#about">Who we are</a></li>
            <li><a href="/index.html#services">Our services</a></li>
            <li><a href="/index.html#clients">Our clients</a></li>
            <li><a href="/contact.html">Contact us</a></li>'''
    new_content = re.sub(company_pattern, new_company, new_content)

    # 4. Update Social links
    social_pattern = re.compile(r'<div class="social-icons">.*?</div>', re.DOTALL)
    social_match = social_pattern.search(new_content)
    if social_match:
        social_html = '''<div class="social-icons">
          <a class="me-2" href="https://in.linkedin.com/company/dashstack-infotech" target="_blank" rel="noopener">
            <img src="./images/linkedin_icon.avif" alt="LinkeDin" />
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
        </div>'''
        new_content = new_content.replace(social_match.group(0), social_html)

    # Make the row visible by removing d-none if it's there
    new_content = new_content.replace('<div class="row g-4 d-none">', '<div class="row g-4 justify-content-between">')
    # Or maybe just `<div class="row g-4">`
    new_content = new_content.replace('<div class="row g-4 justify-content-between">', '<div class="row g-4">')

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Done")
