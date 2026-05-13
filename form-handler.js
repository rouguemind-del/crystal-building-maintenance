// Crystal Building Maintenance - Form Handler
// Sends form submissions to Randy@CrystalBuildingMaintenance.com

// Web3Forms Access Key (free tier - 250 submissions/month)
// This sends to Randy@CrystalBuildingMaintenance.com
const WEB3FORMS_ACCESS_KEY = 'YOUR_ACCESS_KEY_HERE';

// Initialize all forms on the page
function initializeForms() {
    // Handle all quote forms
    const forms = document.querySelectorAll('.quote-form, .contact-form form');
    forms.forEach(form => {
        form.addEventListener('submit', handleFormSubmit);
    });
}

async function handleFormSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const submitBtn = form.querySelector('button[type="submit"], .btn-primary');
    const originalText = submitBtn.textContent;
    
    // Get form data
    const formData = new FormData(form);
    
    // Add metadata
    formData.append('access_key', WEB3FORMS_ACCESS_KEY);
    formData.append('from_name', 'Crystal Building Maintenance Website');
    formData.append('subject', `New Quote Request from ${formData.get('name')}`);
    
    // Add page info
    const currentPage = window.location.pathname.split('/').pop() || 'homepage';
    formData.append('page', currentPage);
    formData.append('timestamp', new Date().toLocaleString('en-US', { timeZone: 'America/New_York' }));
    
    // Basic validation
    const requiredFields = ['name', 'email', 'phone'];
    for (const field of requiredFields) {
        if (!formData.get(field)) {
            showError(`Please fill in the ${field} field`);
            return;
        }
    }
    
    // Email validation
    const email = formData.get('email');
    if (!isValidEmail(email)) {
        showError('Please enter a valid email address');
        return;
    }
    
    // Show loading state
    submitBtn.textContent = 'Sending...';
    submitBtn.disabled = true;
    
    try {
        // Send to Web3Forms API
        const response = await fetch('https://api.web3forms.com/submit', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (data.success) {
            showSuccess('Thank you! Randy will contact you within 24 hours.');
            form.reset();
            
            // Track submission (if analytics is set up)
            if (typeof gtag !== 'undefined') {
                gtag('event', 'form_submit', {
                    'event_category': 'engagement',
                    'event_label': currentPage
                });
            }
        } else {
            throw new Error(data.message || 'Form submission failed');
        }
        
    } catch (error) {
        console.error('Form submission error:', error);
        showError('There was an error sending your message. Please call us at (561) 684-5652');
    } finally {
        // Reset button
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }
}

function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showSuccess(message) {
    // Remove any existing messages
    removeMessages();
    
    // Create success message
    const successDiv = document.createElement('div');
    successDiv.className = 'form-message form-success';
    successDiv.innerHTML = `
        <div style="background: #4CAF50; color: white; padding: 15px; border-radius: 5px; margin: 20px 0;">
            <strong>✓ Success!</strong> ${message}
        </div>
    `;
    
    // Insert after the form
    const form = document.querySelector('.quote-form, .contact-form form');
    if (form) {
        form.parentNode.insertBefore(successDiv, form.nextSibling);
        
        // Auto-remove after 10 seconds
        setTimeout(() => {
            successDiv.remove();
        }, 10000);
    }
}

function showError(message) {
    // Remove any existing messages
    removeMessages();
    
    // Create error message
    const errorDiv = document.createElement('div');
    errorDiv.className = 'form-message form-error';
    errorDiv.innerHTML = `
        <div style="background: #f44336; color: white; padding: 15px; border-radius: 5px; margin: 20px 0;">
            <strong>⚠ Error:</strong> ${message}
        </div>
    `;
    
    // Insert after the form
    const form = document.querySelector('.quote-form, .contact-form form');
    if (form) {
        form.parentNode.insertBefore(errorDiv, form.nextSibling);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            errorDiv.remove();
        }, 5000);
    }
}

function removeMessages() {
    const messages = document.querySelectorAll('.form-message');
    messages.forEach(msg => msg.remove());
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeForms);
} else {
    initializeForms();
}

// Fallback email display (in case JavaScript fails)
document.addEventListener('DOMContentLoaded', function() {
    // Add a visible email link as fallback
    const forms = document.querySelectorAll('.quote-form, .contact-form form');
    forms.forEach(form => {
        const fallback = document.createElement('div');
        fallback.style.cssText = 'margin-top: 10px; font-size: 14px; color: #666;';
        fallback.innerHTML = 'Or email directly: <a href="mailto:Randy@CrystalBuildingMaintenance.com">Randy@CrystalBuildingMaintenance.com</a>';
        form.appendChild(fallback);
    });
});