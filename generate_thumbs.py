import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

data = [
    {"file": "images/symcheck_main_ss.jpg", "title": "Healthexus", "desc": "Secure, intelligent healthcare platform for medical data exchange."},
    {"file": "images/health_gauge_main_ss.jpg", "title": "HealthGauge", "desc": "Comprehensive wellness and health tracking application."},
    {"file": "images/dfx5_main_ss.jpg", "title": "DFX5 AI Care", "desc": "Cloud-native AI contact center for banking support."},
    {"file": "images/123family_ss_main.jpg", "title": "123Family", "desc": "Accessible video calling app designed for seniors."},
    {"file": "images/ultra_main_ss.jpg", "title": "Ultra Messenger", "desc": "Fast, reliable video calling and messaging platform."},
    {"file": "images/urban_swift_main_ss.jpg", "title": "UrbanSwift", "desc": "Enterprise-grade SaaS delivery and logistics platform."},
    {"file": "images/wedo_solar_main_ss.jpg", "title": "WeDoSolar", "desc": "Innovative greentech app for solar technology management."},
    {"file": "images/auramind_main_ss.jpg", "title": "AuraMind", "desc": "Mental wellness app for calm, focus, and mindfulness."},
    {"file": "images/orte_main_ss.jpg", "title": "Orte", "desc": "Fitness and health insights application to optimize performance."},
    {"file": "images/navadiya_owner_main_ss.jpg", "title": "Navadiya Owner", "desc": "Accounting and business management app for owners."},
    {"file": "images/crick_box_ss_main.jpg", "title": "CrickBox", "desc": "Sports venue discovery and booking app for cricket."},
    {"file": "images/ds_dice_main_ss.jpg", "title": "DSDice", "desc": "Interactive dice-rolling application for tabletop gaming."}
]

# Try to load a nice font, fallback to default
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 60)
    font_desc = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30)
except:
    font_title = ImageFont.load_default()
    font_desc = ImageFont.load_default()

for item in data:
    if not os.path.exists(item['file']):
        print("Missing:", item['file'])
        continue
    img = Image.open(item['file']).convert('RGB')
    
    # Create canvas 1200x800, PURE BLACK theme
    canvas = Image.new('RGB', (1200, 800), color='#000000')
    draw = ImageDraw.Draw(canvas)
    
    # Resize screenshot to fit on right
    img.thumbnail((600, 700), Image.Resampling.LANCZOS)
    
    canvas.paste(img, (1150 - img.width, (800 - img.height) // 2))
    
    # Text
    draw.text((80, 300), item['title'], fill='#ffffff', font=font_title)
    
    wrapped_desc = textwrap.fill(item['desc'], width=35)
    draw.text((80, 400), wrapped_desc, fill='#cccccc', font=font_desc, spacing=10)
    
    out_name = item['file'].replace('.jpg', '_horizontal.jpg')
    canvas.save(out_name, quality=90)
    print("Saved", out_name)

