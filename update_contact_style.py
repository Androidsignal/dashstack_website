import glob
import re

html_files = glob.glob('*.html')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace Drop Us An Email
    old_email_html = """                <span class="d-block text-muted">Drop Us An Email</span>
                <a href="mailto:team@dashstack.tech" class="text-decoration-none" style="color: #131313;">team@dashstack.tech</a>"""
    
    new_email_html = """                <span class="d-block" style="color: #8c8c8c; font-size: 16px; margin-bottom: 4px;">Drop Us An Email</span>
                <a href="mailto:team@dashstack.tech" class="text-decoration-none d-block" style="color: #131313; font-size: 22px; font-weight: 400; letter-spacing: 0.5px;">team@dashstack.tech</a>"""
    
    # Replace Call Our Project Experts
    old_phone_html = """                <span class="d-block text-muted">Call Our Project Experts</span>
                <a href="tel:+918153916802" class="text-decoration-none" style="color: #131313;">(+91) 8153 9168 02</a>"""
    
    new_phone_html = """                <span class="d-block" style="color: #8c8c8c; font-size: 16px; margin-bottom: 4px;">Call Our Project Experts</span>
                <a href="tel:+918153916802" class="text-decoration-none d-block" style="color: #131313; font-size: 22px; font-weight: 400; letter-spacing: 0.5px;">(+91) 8153 9168 02</a>"""

    content = content.replace(old_email_html, new_email_html)
    content = content.replace(old_phone_html, new_phone_html)
    
    # Just in case the previous replacement used a different formatting, let's also try regex
    content = re.sub(
        r'<span class="d-block text-muted">Drop Us An Email</span>\s*<a href="mailto:team@dashstack.tech" class="text-decoration-none" style="color: #131313;">team@dashstack.tech</a>',
        new_email_html,
        content
    )
    content = re.sub(
        r'<span class="d-block text-muted">Call Our Project Experts</span>\s*<a href="tel:\+918153916802" class="text-decoration-none" style="color: #131313;">\(\+91\) 8153 9168 02</a>',
        new_phone_html,
        content
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Contact style updated.")
