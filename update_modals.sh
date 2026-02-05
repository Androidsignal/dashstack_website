#!/bin/bash

# List of HTML files to update (excluding the ones already done)
files=(
  "aura-mind.html"
  "antee.html"
  "contact.html"
  "dfx5.html"
  "festigo.html"
  "health_gauge.html"
  "orte.html"
  "urban-swift.html"
  "ultra-messenger.html"
  "we-do-solar.html"
  "123family.html"
  "2i2i.html"
  "amyal.html"
  "crick-admin.html"
  "ds-dice.html"
  "lotus.html"
  "navadiya_owners.html"
  "symcheck.html"
)

for file in "${files[@]}"; do
  if [ -f "$file" ]; then
    echo "Updating $file..."
    
    # First, let's check if it has the old modal pattern and update scripts
    if grep -q 'id="staticBackdrop"' "$file"; then
      echo "  - Removing hardcoded modal..."
      # Use sed to remove the modal section
      sed -i '' '/^  *<!-- Modal -->/,/^  *<!-- Enhanced Footer -->/! { /^  *<!-- Modal -->/! { /^  *<!-- Enhanced Footer -->/! b }; }; /^  *<!-- Modal -->/,/^  *<!-- Enhanced Footer -->/{ /^  *<!-- Enhanced Footer -->/! d }' "$file" 2>/dev/null || true
    fi
  else
    echo "File $file not found"
  fi
done

echo "Done!"
