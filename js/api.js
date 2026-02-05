// Function to send inquiry email
async function submitContactForm(event) {
  event.preventDefault();

  // Get form values
  const fullName = document.getElementById('fullName').value;
  const company = document.getElementById('company').value;
  const email = document.getElementById('email').value;
  const projectDetails = document.getElementById('description').value;

  // Validate form
  if (!fullName || !email || !projectDetails) {
    alert('Please fill in all required fields');
    return;
  }

  // Show loading state
  const submitBtn = event.target.querySelector('button[type="submit"]');
  const originalText = submitBtn.textContent;
  submitBtn.textContent = 'Sending...';
  submitBtn.disabled = true;

  try {
    const response = await fetch('https://sendinquiryemail-775373879129.us-central1.run.app', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: fullName,
        company: company || 'Not provided',
        email: email,
        projectDetails: projectDetails
      })
    });

    if (response.ok) {
      alert('Thank you! We will get back to you soon.');
      event.target.reset(); // Clear form
      // Close modal if it exists
      const modalElement = document.getElementById('staticBackdrop');
      if (modalElement) {
        const modal = bootstrap.Modal.getInstance(modalElement);
        if (modal) {
          modal.hide();
        }
      }
    } else {
      alert('Error submitting form. Please try again.');
    }
  } catch (error) {
    console.error('Error:', error);
    alert('Error submitting form. Please try again.');
  } finally {
    submitBtn.textContent = originalText;
    submitBtn.disabled = false;
  }
}

// Initialize form listener
function initializeContactForm() {
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', submitContactForm);
  }
}

// Run when DOM is ready
document.addEventListener('DOMContentLoaded', initializeContactForm);