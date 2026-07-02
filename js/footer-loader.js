// Load footer HTML into page
async function loadFooter() {
  try {
    const footerPath = './includes/footer.html';
    
    console.log('[Footer Loader] Loading footer from:', footerPath);

    const response = await fetch(footerPath);
    if (response.ok) {
      const footerHTML = await response.text();
      console.log('[Footer Loader] Footer HTML loaded successfully');
      
      const placeholder = document.getElementById('footer-placeholder');
      if (placeholder) {
        placeholder.innerHTML = footerHTML;
        console.log('[Footer Loader] Footer injected into placeholder');
      } else {
        console.error('[Footer Loader] #footer-placeholder not found in DOM');
      }
    } else {
      console.error('[Footer Loader] Failed to load footer from ' + footerPath + '. Status: ' + response.status);
    }
  } catch (error) {
    console.error('[Footer Loader] Error loading footer:', error);
  }
}

// Load footer when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadFooter);
} else {
  loadFooter();
}
