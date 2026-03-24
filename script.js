// Crystal Building Maintenance - Clean Professional JavaScript
// Mobile navigation, form handling, and smooth interactions

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize responsive navigation
    handleResponsiveNav();
    
    // Initialize mobile navigation
    initializeMobileNav();
    
    // Initialize smooth scrolling
    initializeSmoothScrolling();
    
    // Initialize FAQ toggles
    initializeFAQ();
    
    // Initialize contact form
    initializeContactForm();
    
    // Initialize header scroll effects
    initializeHeaderEffects();
    
    // Initialize phone formatting
    initializePhoneFormatting();
    
    // Initialize analytics
    initializeAnalytics();
    
    // Initialize floating button
    initializeFloatingButton();
    
});

// Responsive Navigation Handler
function handleResponsiveNav() {
    const hamburger = document.getElementById('hamburger');
    const navContact = document.querySelector('.nav-contact');
    const navLinks = document.getElementById('navLinks');
    
    function updateNavVisibility() {
        const isMobile = window.innerWidth <= 768;
        
        if (hamburger) {
            hamburger.style.display = isMobile ? 'block' : 'none';
        }
        
        if (navContact) {
            navContact.style.display = isMobile ? 'none' : 'flex';
        }
        
        if (navLinks) {
            navLinks.style.display = isMobile ? 'none' : 'flex';
            navLinks.classList.remove('open'); // Close mobile menu on resize
        }
    }
    
    // Initial check
    updateNavVisibility();
    
    // Handle window resize
    window.addEventListener('resize', updateNavVisibility);
}

// Clean Mobile Navigation (Long Island Wall Pro style)
function initializeMobileNav() {
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');
    
    console.log('Mobile Nav Init:', { hamburger, navLinks });
    
    if (!hamburger || !navLinks) {
        console.error('Missing elements:', { hamburger: !!hamburger, navLinks: !!navLinks });
        return;
    }
    
    // Toggle menu on hamburger click
    hamburger.addEventListener('click', function() {
        console.log('Hamburger clicked, toggling nav-links');
        navLinks.classList.toggle('open');
        console.log('Nav links classes:', navLinks.className);
    });
    
    // Close menu when clicking nav links
    navLinks.querySelectorAll('a').forEach(function(link) {
        link.addEventListener('click', function() {
            navLinks.classList.remove('open');
        });
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!hamburger.contains(event.target) && !navLinks.contains(event.target)) {
            navLinks.classList.remove('open');
        }
    });
}

// Smooth Scrolling
function initializeSmoothScrolling() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                e.preventDefault();
                
                const headerHeight = document.getElementById('header').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// FAQ Toggles
function initializeFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('h3');
        
        if (question) {
            question.addEventListener('click', function() {
                // Close other open items
                faqItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove('active');
                    }
                });
                
                // Toggle current item
                item.classList.toggle('active');
            });
        }
    });
}

// Contact Form
function initializeContactForm() {
    const form = document.querySelector('.quote-form');
    if (!form) return;
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = new FormData(this);
        const data = Object.fromEntries(formData);
        
        // Basic validation
        if (!validateForm(data)) {
            return;
        }
        
        // Show loading state
        const submitBtn = this.querySelector('.btn-primary');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Sending...';
        submitBtn.disabled = true;
        
        // Simulate form submission (replace with actual endpoint)
        setTimeout(() => {
            showSuccessMessage();
            this.reset();
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
        }, 1500);
    });
}

function validateForm(data) {
    const requiredFields = ['name', 'email', 'phone', 'facility-type'];
    const errors = [];
    
    // Check required fields
    requiredFields.forEach(field => {
        if (!data[field] || data[field].trim() === '') {
            errors.push(`${field.replace('-', ' ')} is required`);
        }
    });
    
    // Email validation
    if (data.email && !isValidEmail(data.email)) {
        errors.push('Please enter a valid email address');
    }
    
    // Phone validation
    if (data.phone && !isValidPhone(data.phone)) {
        errors.push('Please enter a valid phone number');
    }
    
    if (errors.length > 0) {
        showErrorMessage(errors);
        return false;
    }
    
    return true;
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPhone(phone) {
    const phoneRegex = /^[\d\s\(\)\-\+\.]{10,}$/;
    return phoneRegex.test(phone);
}

function showErrorMessage(errors) {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.form-message');
    existingMessages.forEach(msg => msg.remove());
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'form-message error-message';
    errorDiv.style.cssText = `
        background: #fee2e2;
        border: 1px solid #fecaca;
        color: #b91c1c;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    `;
    errorDiv.innerHTML = `
        <strong>Please fix the following errors:</strong>
        <ul style="margin: 0.5rem 0 0 1rem;">
            ${errors.map(error => `<li>${error}</li>`).join('')}
        </ul>
    `;
    
    const form = document.querySelector('.quote-form');
    form.insertBefore(errorDiv, form.firstChild);
    
    // Scroll to error
    errorDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function showSuccessMessage() {
    // Remove existing messages
    const existingMessages = document.querySelectorAll('.form-message');
    existingMessages.forEach(msg => msg.remove());
    
    const successDiv = document.createElement('div');
    successDiv.className = 'form-message success-message';
    successDiv.style.cssText = `
        background: #dcfce7;
        border: 1px solid #bbf7d0;
        color: #166534;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        text-align: center;
    `;
    successDiv.innerHTML = `
        <strong>Thank you for your quote request!</strong><br>
        We'll contact you within 2 hours during business hours.
        <br><br>
        <strong>Need immediate service? Call <a href="tel:5616845652" style="color: #166534; font-weight: bold;">(561) 684-5652</a></strong>
    `;
    
    const form = document.querySelector('.quote-form');
    form.insertBefore(successDiv, form.firstChild);
    
    // Auto-remove after 8 seconds
    setTimeout(() => {
        successDiv.remove();
    }, 8000);
    
    // Scroll to success message
    successDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Header Scroll Effects
function initializeHeaderEffects() {
    const header = document.getElementById('header');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            header.style.background = 'rgba(255, 255, 255, 0.95)';
            header.style.backdropFilter = 'blur(10px)';
        } else {
            header.style.background = '#ffffff';
            header.style.backdropFilter = 'none';
        }
    });
}

// Phone Number Formatting
function initializePhoneFormatting() {
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    
    phoneInputs.forEach(input => {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            
            if (value.length >= 10) {
                value = `(${value.slice(0,3)}) ${value.slice(3,6)}-${value.slice(6,10)}`;
            } else if (value.length >= 6) {
                value = `(${value.slice(0,3)}) ${value.slice(3,6)}-${value.slice(6)}`;
            } else if (value.length >= 3) {
                value = `(${value.slice(0,3)}) ${value.slice(3)}`;
            }
            
            e.target.value = value;
        });
    });
}

// Utility function for throttling
function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    }
}

// Track events (placeholder for analytics)
function trackEvent(action, category, label) {
    // Google Analytics 4
    if (typeof gtag !== 'undefined') {
        gtag('event', action, {
            'event_category': category,
            'event_label': label
        });
    }
    
    // Console log for debugging
    console.log('Event tracked:', { action, category, label });
}

// Initialize analytics tracking
function initializeAnalytics() {
    // Track phone clicks
    const phoneLinks = document.querySelectorAll('a[href^="tel:"]');
    phoneLinks.forEach(link => {
        link.addEventListener('click', function() {
            trackEvent('phone_call', 'engagement', 'contact_phone');
        });
    });
    
    // Track form submissions
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            trackEvent('form_submission', 'lead', 'contact_form');
        });
    });
    
    // Track CTA button clicks
    const ctaButtons = document.querySelectorAll('.btn-primary, .btn-secondary');
    ctaButtons.forEach(button => {
        button.addEventListener('click', function() {
            const text = this.textContent.toLowerCase();
            if (text.includes('quote')) {
                trackEvent('cta_click', 'engagement', 'get_quote');
            } else if (text.includes('call')) {
                trackEvent('cta_click', 'engagement', 'call_now');
            }
        });
    });
}

// Initialize analytics on load
initializeAnalytics();

// Add scroll-based animations
function initializeScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animatedElements = document.querySelectorAll('.service-card, .area-card, .testimonial');
    animatedElements.forEach(element => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(20px)';
        element.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(element);
    });
}

// Initialize scroll animations
initializeScrollAnimations();

// Floating Call Button Handler
function initializeFloatingButton() {
    const floatingBtn = document.querySelector('.floating-call-btn');
    
    if (!floatingBtn) return;
    
    // Add entrance animation (but keep button always visible after)
    setTimeout(() => {
        floatingBtn.style.opacity = '0';
        floatingBtn.style.transform = 'translateY(100px) !important';
        floatingBtn.style.transition = 'all 0.6s ease';
        
        setTimeout(() => {
            floatingBtn.style.opacity = '1';
            floatingBtn.style.transform = 'none !important';
            // Ensure button stays visible
            floatingBtn.style.position = 'fixed';
            floatingBtn.style.bottom = '30px';
            floatingBtn.style.right = '30px';
        }, 1000);
    }, 100);
    
    // Track floating button clicks
    floatingBtn.addEventListener('click', function() {
        trackEvent('floating_call_button', 'engagement', 'call_now_floating');
        
        // Add click animation
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = '';
        }, 150);
    });
    
    // Keep button always visible - no scroll hiding behavior
    // Button stays fixed in position at all times
}