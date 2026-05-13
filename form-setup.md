# Crystal Building Maintenance - Form Setup Guide

## Current Setup: FormSubmit.co Integration

I've set up the contact forms to send directly to Randy's email using FormSubmit.co - a free service that doesn't require API keys or registration.

### How It Works:
1. Forms submit to: `https://formsubmit.co/Randy@CrystalBuildingMaintenance.com`
2. FormSubmit sends the form data to Randy's email
3. First-time setup requires email verification (one-time only)

### To Complete Setup:

1. **Email Verification (Randy needs to do this once):**
   - The first form submission will trigger a verification email to Randy@CrystalBuildingMaintenance.com
   - Randy needs to click the verification link in that email
   - After verification, all future submissions will go directly to his inbox

2. **Test the Form:**
   - Go to any page with a contact form (e.g., https://test.crystalbuildingmaintenance.com/contact.html)
   - Fill out and submit the form
   - Randy should receive the verification email

3. **Optional Enhancements:**
   - Add a thank you page redirect
   - Set up auto-responders
   - Add CC recipients (like Rob@CrystalBuildingMaintenance.com)

### Files Modified:
- `form-handler-simple.js` - New form handler using FormSubmit
- All HTML pages with forms will use this handler

### Form Features:
✅ No API keys needed
✅ Free forever (unlimited submissions)
✅ Spam protection built-in
✅ Works with static sites
✅ Email verification prevents abuse
✅ Includes all form fields in email
✅ Mobile responsive

### Backup Contact Methods:
- Direct email: Randy@CrystalBuildingMaintenance.com
- Phone: (561) 684-5652

### Next Steps:
1. Push changes to GitHub
2. Wait for GoDaddy sync
3. Have Randy verify the email when first submission comes through
4. Forms are live!

---
*Note: The form will show "Sending..." then display a success message. The actual email delivery happens server-side through FormSubmit.*