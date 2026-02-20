"""
Test forms and user interactions
"""
import pytest
import logging
from playwright.sync_api import Page, expect

logger = logging.getLogger('zanethemba_tests.forms')


class TestContactForm:
    """Test contact form functionality"""
    
    @pytest.mark.smoke
    def test_contact_form_visible(self, page):
        """Test contact form is visible"""
        logger.info("Testing contact form visibility")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        form = page.locator("#contactForm")
        expect(form).to_be_visible()
        
        logger.info("Contact form is visible")
    
    @pytest.mark.regression
    def test_form_has_all_fields(self, page):
        """Test contact form has all required fields"""
        logger.info("Testing contact form fields")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Check for all form fields
        fields = ["fname", "lname", "email", "phone", "service", "message"]
        
        for field_id in fields:
            field = page.locator(f"#{field_id}")
            expect(field).to_be_visible()
            logger.info(f"Field '{field_id}' is present")
    
    @pytest.mark.regression
    def test_form_labels_present(self, page):
        """Test form labels are present"""
        logger.info("Testing form labels")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        labels = ["First Name", "Last Name", "Email Address", "Phone Number"]
        
        for label_text in labels:
            label = page.locator(f"label:has-text('{label_text}')")
            expect(label).to_be_visible()
            logger.info(f"Label '{label_text}' is visible")
    
    @pytest.mark.regression
    def test_service_dropdown_options(self, page):
        """Test service dropdown has options"""
        logger.info("Testing service dropdown options")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        service_select = page.locator("#service")
        expect(service_select).to_be_visible()
        
        # Check dropdown has options
        options = page.locator("#service option")
        count = options.count()
        assert count > 1, f"Expected multiple service options, got {count}"
        
        logger.info(f"Service dropdown has {count} options")
    
    @pytest.mark.regression
    def test_form_submission_happy_path(self, page):
        """Test successful form submission"""
        logger.info("Testing form submission (happy path)")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Fill out the form
        page.fill("#fname", "John")
        page.fill("#lname", "Doe")
        page.fill("#email", "john.doe@example.com")
        page.fill("#phone", "+27 82 123 4567")
        page.select_option("#service", "Residential Cleaning")
        page.fill("#message", "I would like to request a quote for residential cleaning services.")
        
        logger.info("Form filled with valid data")
        
        # Submit the form
        submit_button = page.locator("button[type='submit']")
        submit_button.click()
        page.wait_for_timeout(500)
        
        # Check for success message
        success_div = page.locator("#formSuccess")
        expect(success_div).to_be_visible()
        
        success_message = page.locator(".form-success h3")
        expect(success_message).to_have_text("Message Sent!")
        
        logger.info("Form submission successful, success message displayed")
    
    @pytest.mark.negative
    def test_form_requires_first_name(self, page):
        """Test form validates first name is required"""
        logger.info("Testing first name validation")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Try to submit without first name
        page.fill("#lname", "Doe")
        page.fill("#email", "john@example.com")
        
        fname_field = page.locator("#fname")
        
        # Check if field is required
        is_required = fname_field.get_attribute("required")
        assert is_required is not None, "First name field should be required"
        
        logger.info("First name field is properly marked as required")
    
    @pytest.mark.negative
    def test_form_requires_last_name(self, page):
        """Test form validates last name is required"""
        logger.info("Testing last name validation")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        lname_field = page.locator("#lname")
        is_required = lname_field.get_attribute("required")
        assert is_required is not None, "Last name field should be required"
        
        logger.info("Last name field is properly marked as required")
    
    @pytest.mark.negative
    def test_form_requires_email(self, page):
        """Test form validates email is required"""
        logger.info("Testing email validation")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        email_field = page.locator("#email")
        is_required = email_field.get_attribute("required")
        assert is_required is not None, "Email field should be required"
        
        field_type = email_field.get_attribute("type")
        assert field_type == "email", "Email field should be type='email'"
        
        logger.info("Email field has proper validation")
    
    @pytest.mark.negative
    def test_phone_field_optional(self, page):
        """Test phone field is optional"""
        logger.info("Testing phone field is optional")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        phone_field = page.locator("#phone")
        is_required = phone_field.get_attribute("required")
        assert is_required is None, "Phone field should be optional"
        
        logger.info("Phone field is correctly optional")
    
    @pytest.mark.regression
    def test_form_placeholders(self, page):
        """Test form fields have placeholders"""
        logger.info("Testing form field placeholders")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Check some placeholders
        fname = page.locator("#fname")
        fname_placeholder = fname.get_attribute("placeholder")
        assert fname_placeholder == "Your first name", "First name should have placeholder"
        
        email = page.locator("#email")
        email_placeholder = email.get_attribute("placeholder")
        assert "email.com" in email_placeholder, "Email should have example placeholder"
        
        logger.info("Form placeholders are present")


class TestCTAButtons:
    """Test Call-to-Action buttons"""
    
    @pytest.mark.regression
    def test_hero_cta_navigates_to_contact(self, page):
        """Test hero CTA button navigates to contact page"""
        logger.info("Testing hero CTA navigation")
        
        cta_button = page.get_by_role("link", name="Request a Service")
        cta_button.click()
        page.wait_for_timeout(500)
        
        contact_page = page.locator("#page-contact")
        expect(contact_page).to_have_class("page active")
        
        logger.info("Hero CTA successfully navigates to Contact page")
    
    @pytest.mark.regression
    def test_our_story_cta_navigates_to_about(self, page):
        """Test 'Our Story' CTA navigates to About page"""
        logger.info("Testing 'Our Story' CTA navigation")
        
        cta_button = page.get_by_role("link", name="Our Story")
        cta_button.click()
        page.wait_for_timeout(500)
        
        about_page = page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        
        logger.info("'Our Story' CTA successfully navigates to About page")
    
    @pytest.mark.regression
    def test_service_card_cta(self, page):
        """Test service card CTA button"""
        logger.info("Testing service card CTA")
        
        # Find the 'Talk to Us' button in service card
        talk_to_us = page.get_by_role("link", name="Talk to Us")
        talk_to_us.click()
        page.wait_for_timeout(500)
        
        contact_page = page.locator("#page-contact")
        expect(contact_page).to_have_class("page active")
        
        logger.info("Service card CTA navigates to Contact page")
    
    @pytest.mark.regression
    def test_community_learn_story_cta(self, page):
        """Test community section 'Learn Our Story' CTA"""
        logger.info("Testing community section CTA")
        
        learn_story = page.get_by_role("link", name="Learn Our Story")
        learn_story.click()
        page.wait_for_timeout(500)
        
        about_page = page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        
        logger.info("Community CTA navigates to About page")


class TestLinks:
    """Test external and internal links"""
    
    @pytest.mark.regression
    def test_email_link_has_mailto(self, page):
        """Test email links have mailto: protocol"""
        logger.info("Testing email link protocol")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        email_link = page.locator("a[href='mailto:info@zanethembacleaning.co.za']").first
        expect(email_link).to_be_visible()
        
        href = email_link.get_attribute("href")
        assert href.startswith("mailto:"), "Email link should use mailto: protocol"
        
        logger.info("Email links use correct mailto: protocol")
    
    @pytest.mark.regression
    def test_phone_links_have_tel(self, page):
        """Test phone links have tel: protocol"""
        logger.info("Testing phone link protocol")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        phone_link = page.locator("a[href='tel:+27615460770']").first
        expect(phone_link).to_be_visible()
        
        href = phone_link.get_attribute("href")
        assert href.startswith("tel:"), "Phone link should use tel: protocol"
        
        logger.info("Phone links use correct tel: protocol")
    
    @pytest.mark.regression
    def test_whatsapp_link(self, page):
        """Test WhatsApp link is correct"""
        logger.info("Testing WhatsApp link")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        whatsapp_link = page.locator("a[href='https://wa.me/27733715083']").first
        expect(whatsapp_link).to_be_visible()
        
        logger.info("WhatsApp link is present and correct")
    
    @pytest.mark.regression
    def test_linkedin_link_opens_new_tab(self, page):
        """Test LinkedIn link has target=_blank"""
        logger.info("Testing LinkedIn link target")
        
        linkedin_link = page.locator("a[href*='linkedin']").first
        expect(linkedin_link).to_be_visible()
        
        target = linkedin_link.get_attribute("target")
        assert target == "_blank", "LinkedIn link should open in new tab"
        
        rel = linkedin_link.get_attribute("rel")
        assert "noopener" in rel, "LinkedIn link should have noopener"
        
        logger.info("LinkedIn link properly configured for new tab")
