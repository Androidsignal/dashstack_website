#!/bin/bash

# Add mouse tracker to all HTML pages
# This script adds the mouse tracker CSS, HTML elements, and JS to all pages

pages=(
  "contact.html"
  "blog.html"
  "123family.html"
  "2i2i.html"
  "amyal.html"
  "antee.html"
  "aura-mind.html"
  "crick-admin.html"
  "crick-box.html"
  "dashwoop.html"
  "dfx5.html"
  "ds-dice.html"
  "festigo.html"
  "health_gauge.html"
  "lotus.html"
  "navadiya_owners.html"
  "orte.html"
  "symcheck.html"
  "ultra-messenger.html"
  "urban-swift.html"
  "we-do-solar.html"
  "landing_page.html"
)

for page in "${pages[@]}"; do
  if [ -f "$page" ]; then
    echo "Processing $page..."
    
    # Check if mouse-tracker.css is already linked
    if ! grep -q "mouse-tracker.css" "$page"; then
      # Add CSS link before </head>
      sed -i.bak 's|</head>|  <link rel="stylesheet" href="./css/mouse-tracker.css" />\n</head>|' "$page"
      echo "  ✓ Added CSS link"
    else
      echo "  - CSS already linked"
    fi
    
    # Check if mouse tracker elements exist
    if ! grep -q 'id="mouseLight"' "$page"; then
      # Add HTML elements after <body> tag
      sed -i.bak 's|<body[^>]*>|&\n<div class="mouse-light" id="mouseLight"></div>\n<div class="mouse-light-inner" id="mouseLightInner"></div>\n<div class="mouse-ring" id="mouseRing"></div>|' "$page"
      echo "  ✓ Added HTML elements"
    else
      echo "  - HTML elements already exist"
    fi
    
    # Check if JS is already linked
    if ! grep -q "mouse-tracker.js" "$page"; then
      # Add JS before </body>
      sed -i.bak 's|</body>|  <script src="./js/mouse-tracker.js"></script>\n</body>|' "$page"
      echo "  ✓ Added JS script"
    else
      echo "  - JS already linked"
    fi
    
  else
    echo "⚠ $page not found"
  fi
done

# Process all blog post pages
for blogpost in blog-post-*.html; do
  if [ -f "$blogpost" ]; then
    echo "Processing $blogpost..."
    
    if ! grep -q "mouse-tracker.css" "$blogpost"; then
      sed -i.bak 's|</head>|  <link rel="stylesheet" href="./css/mouse-tracker.css" />\n</head>|' "$blogpost"
      echo "  ✓ Added CSS link"
    fi
    
    if ! grep -q 'id="mouseLight"' "$blogpost"; then
      sed -i.bak 's|<body[^>]*>|&\n<div class="mouse-light" id="mouseLight"></div>\n<div class="mouse-light-inner" id="mouseLightInner"></div>\n<div class="mouse-ring" id="mouseRing"></div>|' "$blogpost"
      echo "  ✓ Added HTML elements"
    fi
    
    if ! grep -q "mouse-tracker.js" "$blogpost"; then
      sed -i.bak 's|</body>|  <script src="./js/mouse-tracker.js"></script>\n</body>|' "$blogpost"
      echo "  ✓ Added JS script"
    fi
  fi
done

# Remove backup files
rm -f *.bak

echo ""
echo "✅ Mouse tracker setup complete!"
echo "Files updated: ${#pages[@]} main pages + blog posts"
