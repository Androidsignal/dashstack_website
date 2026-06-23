import os
from PIL import Image, ImageDraw, ImageFont

data = [
    "Symcheck Vitals", "HealthGauge", "DFX5 AI Care", "123Family",
    "Ultra Messenger", "UrbanSwift", "WeDoSolar", "AuraMind",
    "Orte", "Navadiya Owner", "CrickBox", "DSDice"
]

try:
    font_logo = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 30)
except:
    font_logo = ImageFont.load_default()

for name in data:
    canvas = Image.new('RGB', (200, 100), color='#ffffff')
    draw = ImageDraw.Draw(canvas)
    
    # Just draw the first letter or initials in center
    initials = "".join([word[0] for word in name.split()[:2]]).upper()
    
    # Try to center it roughly
    draw.text((60, 30), initials, fill='#3b82f6', font=font_logo)
    
    filename = name.lower().replace(' ', '_') + "_logo.jpg"
    out_name = os.path.join("images", filename)
    canvas.save(out_name, quality=90)
    print("Saved logo:", out_name)

