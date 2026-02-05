// Load modal HTML into page
async function loadModal() {
  try {
    // Determine the path based on current page location
    const currentPath = window.location.pathname;
    const isRootPage = currentPath === '/' || currentPath.endsWith('index.html');
    const modalPath = isRootPage ? './includes/modal.html' : '../includes/modal.html';

    const response = await fetch(modalPath);
    if (response.ok) {
      const modalHTML = await response.text();
      
      // Create a container for the modal at the end of body
      const modalContainer = document.createElement('div');
      modalContainer.innerHTML = modalHTML;
      
      // Append to body
      document.body.appendChild(modalContainer.firstElementChild);

      // Re-initialize form listeners after modal is loaded
      initializeContactForm();
    } else {
      console.error('Failed to load modal');
    }
  } catch (error) {
    console.error('Error loading modal:', error);
  }
}

// Load modal when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadModal);
} else {
  loadModal();
}