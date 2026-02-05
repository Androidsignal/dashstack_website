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
    Swal.fire({
      icon: 'warning',
      title: 'Missing Fields',
      text: 'Please fill in all required fields',
      confirmButtonColor: '#10b981'
    });
    return;
  }

  // Show loading spinner
  Swal.fire({
    title: 'Sending Your Inquiry...',
    text: 'Please wait, this may take a moment...',
    allowOutsideClick: false,
    allowEscapeKey: false,
    didOpen: async () => {
      Swal.showLoading();
      
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
          Swal.fire({
            icon: 'success',
            title: 'Thank You!',
            text: 'Your inquiry has been sent successfully. We will get back to you soon.',
            confirmButtonColor: '#10b981'
          });
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
          Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Error submitting form. Please try again.',
            confirmButtonColor: '#10b981'
          });
        }
      } catch (error) {
        console.error('Error:', error);
        Swal.fire({
          icon: 'error',
          title: 'Error',
          text: 'Error submitting form. Please try again.',
          confirmButtonColor: '#10b981'
        });
      }
    }
  });
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