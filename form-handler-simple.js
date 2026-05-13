// Crystal Building Maintenance - Simple Form Handler
// Uses FormSubmit.co to send forms to Randy@CrystalBuildingMaintenance.com
// No API key required - just email verification on first use

document.addEventListener('DOMContentLoaded', function() {
    // Update all forms to use FormSubmit
    const forms = document.querySelectorAll('.quote-form, form');
    
    forms.forEach(form => {
        // Skip if already has an action
        if (form.action && form.action !== '' && !form.action.includes('localhost')) {
            return;
        }
        
        // Set FormSubmit as the action
        form.action = 'https://formsubmit.co/Randy@CrystalBuildingMaintenance.com';
        form.method = 'POST';
        
        // Add hidden fields for better email formatting
        addHiddenField(form, '_subject', 'New Quote Request from Crystal Building Maintenance Website');
        addHiddenField(form, '_template', 'table');
        addHiddenField(form, '_captcha', 'false'); // Disable captcha for better UX
        addHiddenField(form, '_next', window.location.href + '#thank-you');
        
        // Add current page info
        const pageName = window.location.pathname.split('/').pop().replace('.html', '').replace(/-/g, ' ');
        addHiddenField(form, 'Submitted_From_Page', pageName || 'Homepage');
        
        // Handle form submission
        form.addEventListener('submit', function(e) {
            // Don't prevent default - let it submit normally to FormSubmit
            
            // Basic validation
            const name = form.querySelector('[name="name"]');
            const email = form.querySelector('[name="email"]');
            const phone = form.querySelector('[name="phone"]');
            
            if (name && !name.value.trim()) {
                e.preventDefault();
                alert('Please enter your name');
                name.focus();
                return false;
            }
            
            if (email && !isValidEmail(email.value)) {
                e.preventDefault();
                alert('Please enter a valid email address');
                email.focus();
                return false;
            }
            
            if (phone && !phone.value.trim()) {
                e.preventDefault();
                alert('Please enter your phone number');
                phone.focus();
                return false;
            }
            
            // Update button to show sending
            const submitBtn = form.querySelector('button[type="submit"], .btn-primary');
            if (submitBtn) {
                submitBtn.textContent = 'Sending...';
                submitBtn.disabled = true;
                
                // Re-enable after a delay (in case they navigate back)
                setTimeout(() => {
                    submitBtn.textContent = 'Get Free Quote';
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    });
    
    // Check if we're returning from a form submission
    if (window.location.hash === '#thank-you') {
        showThankYouMessage();
        // Remove the hash
        history.replaceState(null, null, window.location.pathname);
    }
});

function addHiddenField(form, name, value) {
    // Check if field already exists
    let field = form.querySelector(`input[name="${name}"]`);
    if (!field) {
        field = document.createElement('input');
        field.type = 'hidden';
        field.name = name;
        form.appendChild(field);
    }
    field.value = value;
}

function isValidEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showThankYouMessage() {
    // Create thank you modal
    const modal = document.createElement('div');
    modal.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: white;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        z-index: 10000;
        max-width: 500px;
        text-align: center;
    `;
    
    modal.innerHTML = `
        <div style="color: #4CAF50; font-size: 48px; margin-bottom: 20px;">✓</div>
        <h2 style="color: #333; margin-bottom: 10px;">Thank You!</h2>
        <p style="color: #666; margin-bottom: 20px;">Your request has been received. Randy will contact you within 24 hours to discuss your cleaning needs.</p>
        <p style="color: #333; font-weight: bold; margin-bottom: 20px;">For immediate assistance, call:<br>
        <a href="tel:5616845652" style="color: #0066cc; font-size: 20px; text-decoration: none;">(561) 684-5652</a></p>
        <button onclick="this.parentElement.remove(); document.getElementById('modal-overlay').remove();" 
                style="background: #0066cc; color: white; border: none; padding: 10px 30px; border-radius: 5px; cursor: pointer; font-size: 16px;">
            Close
        </button>
    `;
    
    // Create overlay
    const overlay = document.createElement('div');
    overlay.id = 'modal-overlay';
    overlay.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.5);
        z-index: 9999;
    `;
    
    overlay.onclick = function() {
        modal.remove();
        overlay.remove();
    };
    
    document.body.appendChild(overlay);
    document.body.appendChild(modal);
    
    // Auto close after 10 seconds
    setTimeout(() => {
        if (document.body.contains(modal)) {
            modal.remove();
            overlay.remove();
        }
    }, 10000);
}