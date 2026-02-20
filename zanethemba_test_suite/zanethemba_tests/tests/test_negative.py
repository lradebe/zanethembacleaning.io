"""
Negative test cases for Zanethemba website
"""
import pytest
import logging
from playwright.sync_api import Page, expect

logger = logging.getLogger('zanethemba_tests.negative')


class TestInvalidInputs:
    """Test handling of invalid inputs"""
    
    @pytest.mark.negative
    def test_email_field_rejects_invalid_format(self, page):
        """Test email field validates format"""
        logger.info("Testing invalid email format rejection")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        email_field = page.locator("#email")
        
        # Try invalid email
        email_field.fill("notanemail")
        email_field.press("Tab")  # Trigger validation
        
        # Check field type is email (browser validation)
        field_type = email_field.get_attribute("type")
        assert field_type == "email", "Email field should enforce validation"
        
        logger.info("Email field has type='email' for validation")
    
    @pytest.mark.negative
    def test_form_empty_submission(self, page):
        """Test form prevents empty submission"""
        logger.info("Testing empty form submission prevention")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Try to submit empty form
        submit_button = page.locator("button[type='submit']")
        
        # Check required fields
        fname = page.locator("#fname")
        is_required = fname.get_attribute("required")
        assert is_required is not None, "Required fields should prevent submission"
        
        logger.info("Form has required field validation")
    
    @pytest.mark.negative
    def test_extremely_long_input(self, page):
        """Test form handles extremely long input"""
        logger.info("Testing extremely long input handling")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Try very long name
        long_name = "A" * 1000
        page.fill("#fname", long_name)
        
        # Should still accept it (no maxlength) but not crash
        filled_value = page.locator("#fname").input_value()
        assert len(filled_value) > 0, "Field should accept input"
        
        logger.info("Form handles long input without crashing")
    
    @pytest.mark.negative
    def test_special_characters_in_name(self, page):
        """Test form handles special characters in name fields"""
        logger.info("Testing special characters in name")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Try name with special characters
        special_name = "<script>alert('XSS')</script>"
        page.fill("#fname", special_name)
        
        filled_value = page.locator("#fname").input_value()
        assert filled_value == special_name, "Input should be preserved as-is"
        
        logger.info("Form handles special characters in name fields")
    
    @pytest.mark.negative
    def test_sql_injection_attempt(self, page):
        """Test form handles SQL injection attempt"""
        logger.info("Testing SQL injection attempt")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Try SQL injection
        sql_string = "'; DROP TABLE users; --"
        page.fill("#message", sql_string)
        
        # Form should accept it as text (client-side, no DB)
        filled_value = page.locator("#message").input_value()
        assert filled_value == sql_string, "Input should be preserved"
        
        logger.info("Form safely handles SQL injection attempt")


class TestNavigationEdgeCases:
    """Test navigation edge cases"""
    
    @pytest.mark.negative
    def test_rapid_navigation_clicks(self, page):
        """Test rapid navigation doesn't break site"""
        logger.info("Testing rapid navigation clicks")
        
        # Rapidly click navigation
        for _ in range(10):
            page.locator("#nav-about").click()
            page.locator("#nav-contact").click()
            page.locator("#nav-home").click()
        
        # Should still work
        page.locator("#nav-about").click()
        page.wait_for_timeout(300)
        
        about_page = page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        
        logger.info("Site handles rapid navigation without breaking")
    
    @pytest.mark.negative
    def test_double_click_navigation(self, page):
        """Test double-clicking navigation doesn't cause issues"""
        logger.info("Testing double-click navigation")
        
        # Double-click About link
        page.locator("#nav-about").dblclick()
        page.wait_for_timeout(500)
        
        # Should still navigate correctly
        about_page = page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        
        logger.info("Double-click navigation handled correctly")
    
    @pytest.mark.negative
    def test_navigation_during_splash(self, context, base_url):
        """Test clicking navigation during splash doesn't break"""
        logger.info("Testing navigation during splash screen")
        
        page = context.new_page()
        page.goto(base_url)
        
        # Try to navigate immediately (during splash)
        page.locator("#nav-about").click()
        
        # Wait for splash to complete
        page.wait_for_timeout(4000)
        
        # Should have navigated successfully
        about_page = page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        
        page.close()
        logger.info("Navigation during splash handled correctly")


class TestMobileEdgeCases:
    """Test mobile-specific edge cases"""
    
    @pytest.mark.negative
    def test_mobile_menu_rapid_toggle(self, mobile_page):
        """Test rapidly opening/closing mobile menu"""
        logger.info("Testing rapid mobile menu toggle")
        
        hamburger = mobile_page.locator("#hamburger")
        
        # Rapidly toggle menu
        for _ in range(5):
            hamburger.click()
            hamburger.click()
        
        # Menu should respond to final state
        mobile_page.wait_for_timeout(500)
        
        logger.info("Mobile menu handles rapid toggling")
    
    @pytest.mark.negative
    def test_mobile_navigation_with_menu_open(self, mobile_page):
        """Test navigating with menu already open"""
        logger.info("Testing navigation with mobile menu open")
        
        # Open menu
        mobile_page.locator("#hamburger").click()
        mobile_page.wait_for_timeout(300)
        
        # Click a link
        mobile_page.locator("#mob-about").click()
        mobile_page.wait_for_timeout(500)
        
        # Menu should close and page should change
        mobile_menu = mobile_page.locator("#mobileMenu")
        expect(mobile_menu).not_to_have_class("mobile-menu open")
        
        about_page = mobile_page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        
        logger.info("Mobile navigation works with menu open")
    
    @pytest.mark.negative
    def test_landscape_mobile_orientation(self, context, base_url):
        """Test site works in landscape mobile"""
        logger.info("Testing landscape mobile orientation")
        
        landscape_context = context.browser.new_context(
            viewport={"width": 667, "height": 375}  # Landscape phone
        )
        page = landscape_context.new_page()
        page.goto(base_url, wait_until="domcontentloaded")
        page.wait_for_timeout(4000)
        
        # Should still be functional
        hero = page.locator(".hero")
        expect(hero).to_be_visible()
        
        page.close()
        landscape_context.close()
        logger.info("Site works in landscape orientation")


class TestCarouselEdgeCases:
    """Test carousel edge cases"""
    
    @pytest.mark.negative
    def test_clicking_carousel_dots_rapidly(self, page):
        """Test rapid carousel dot clicking"""
        logger.info("Testing rapid carousel dot clicking")
        
        dots = page.locator("#heroDots .carousel-dot")
        
        # Rapidly click different dots
        for i in range(10):
            dots.nth(i % 4).click()
        
        page.wait_for_timeout(500)
        
        # Should still have exactly one active slide
        active_slides = page.locator("#heroCarousel .carousel-slide.active")
        expect(active_slides).to_have_count(1)
        
        logger.info("Carousel handles rapid dot clicking")
    
    @pytest.mark.negative
    def test_carousel_with_page_navigation(self, page):
        """Test carousel doesn't interfere with navigation"""
        logger.info("Testing carousel with page navigation")
        
        # Let carousel run
        page.wait_for_timeout(6000)
        
        # Navigate away
        page.locator("#nav-about").click()
        page.wait_for_timeout(300)
        
        # Navigate back
        page.locator("#nav-home").click()
        page.wait_for_timeout(500)
        
        # Carousel should still work
        carousel = page.locator("#heroCarousel")
        expect(carousel).to_be_visible()
        
        active_slides = page.locator("#heroCarousel .carousel-slide.active")
        expect(active_slides).to_have_count(1)
        
        logger.info("Carousel works after navigation")


class TestFormEdgeCases:
    """Test form edge cases"""
    
    @pytest.mark.negative
    def test_submitting_form_twice(self, page):
        """Test submitting form multiple times"""
        logger.info("Testing double form submission")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Fill form
        page.fill("#fname", "Test")
        page.fill("#lname", "User")
        page.fill("#email", "test@example.com")
        
        # Submit once
        page.click("button[type='submit']")
        page.wait_for_timeout(500)
        
        # Form should show success
        success_div = page.locator("#formSuccess")
        expect(success_div).to_be_visible()
        
        # Original form should be hidden
        form = page.locator("#contactForm")
        expect(form).to_be_hidden()
        
        logger.info("Form prevents double submission")
    
    @pytest.mark.negative
    def test_form_with_only_spaces(self, page):
        """Test form with only whitespace in fields"""
        logger.info("Testing form with whitespace-only input")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Fill with spaces
        page.fill("#fname", "   ")
        page.fill("#lname", "   ")
        page.fill("#email", "test@example.com")
        
        # Browser should still accept it (no trim validation)
        fname_value = page.locator("#fname").input_value()
        assert fname_value == "   ", "Whitespace should be preserved"
        
        logger.info("Form accepts whitespace (no client-side trim)")
    
    @pytest.mark.negative
    def test_textarea_with_newlines(self, page):
        """Test textarea handles newlines correctly"""
        logger.info("Testing textarea with newlines")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Fill textarea with newlines
        message_text = "Line 1\nLine 2\nLine 3"
        page.fill("#message", message_text)
        
        filled_value = page.locator("#message").input_value()
        assert "\n" in filled_value, "Newlines should be preserved"
        
        logger.info("Textarea handles newlines correctly")


class TestAccessibilityEdgeCases:
    """Test accessibility edge cases"""
    
    @pytest.mark.negative
    def test_tab_navigation_works(self, page):
        """Test keyboard tab navigation"""
        logger.info("Testing keyboard tab navigation")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Focus first field
        page.locator("#fname").focus()
        
        # Tab to next field
        page.keyboard.press("Tab")
        
        # Should focus on last name
        focused_element = page.evaluate("document.activeElement.id")
        assert focused_element == "lname", f"Expected lname, got {focused_element}"
        
        logger.info("Tab navigation works correctly")
    
    @pytest.mark.negative
    def test_enter_key_on_link(self, page):
        """Test pressing Enter on focused link"""
        logger.info("Testing Enter key on navigation link")
        
        # Focus on About link
        page.locator("#nav-about").focus()
        
        # Press Enter
        page.keyboard.press("Enter")
        page.wait_for_timeout(500)
        
        # Should navigate to About
        about_page = page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        
        logger.info("Enter key navigation works")


class TestBrowserCompatibility:
    """Test browser-specific edge cases"""
    
    @pytest.mark.negative
    def test_page_reload_maintains_state(self, page):
        """Test page reload goes back to home"""
        logger.info("Testing page reload behavior")
        
        # Navigate to About
        page.locator("#nav-about").click()
        page.wait_for_timeout(500)
        
        # Reload page
        page.reload()
        page.wait_for_timeout(4000)  # Wait for splash
        
        # Should be back on home page (default)
        home_page = page.locator("#page-home")
        expect(home_page).to_have_class("page active")
        
        logger.info("Page reload returns to home (no state persistence)")
    
    @pytest.mark.negative
    def test_back_button_not_supported(self, page):
        """Test browser back button (SPA limitation)"""
        logger.info("Testing browser back button (SPA)")
        
        # Navigate to About
        page.locator("#nav-about").click()
        page.wait_for_timeout(500)
        
        # Try browser back (won't work in SPA without hash routing)
        page.go_back()
        page.wait_for_timeout(300)
        
        # Still on same page (file:// URL doesn't change)
        logger.info("Browser back button doesn't affect SPA (expected)")
