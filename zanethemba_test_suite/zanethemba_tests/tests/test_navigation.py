"""
Test navigation and UI elements of Zanethemba website
"""
import pytest
import logging
from playwright.sync_api import Page, expect

logger = logging.getLogger('zanethemba_tests.navigation')


class TestNavigation:
    """Test navigation functionality"""
    
    @pytest.mark.smoke
    def test_splash_screen_appears(self, context, base_url):
        """Test that splash screen appears on load"""
        logger.info("Testing splash screen appearance")
        page = context.new_page()
        page.goto(base_url)
        
        # Splash should be visible immediately
        splash = page.locator("#splash")
        expect(splash).to_be_visible()
        logger.info("Splash screen is visible on load")
        
        # Wait for it to fade out
        page.wait_for_timeout(4000)
        expect(splash).to_have_css("display", "none")
        logger.info("Splash screen fades out correctly")
        
        page.close()
    
    @pytest.mark.smoke
    def test_logo_visible_in_nav(self, page):
        """Test that logo is visible in navigation"""
        logger.info("Testing logo visibility in navigation")
        logo = page.locator(".nav-logo img")
        expect(logo).to_be_visible()
        logger.info("Logo is visible in navigation")
    
    @pytest.mark.smoke
    def test_company_name_visible_in_nav(self, page):
        """Test company name appears next to logo"""
        logger.info("Testing company name in navigation")
        brand_main = page.locator(".brand-main")
        expect(brand_main).to_have_text("Zanethemba")
        
        brand_sub = page.locator(".brand-sub")
        expect(brand_sub).to_have_text("Cleaning Services")
        logger.info("Company name correctly displayed")
    
    @pytest.mark.smoke
    def test_navigation_links_present(self, page):
        """Test all navigation links are present"""
        logger.info("Testing navigation links presence")
        
        nav_links = ["Home", "About Us", "Contact Us"]
        for link_text in nav_links:
            link = page.get_by_role("link", name=link_text, exact=True)
            expect(link).to_be_visible()
            logger.info(f"Navigation link '{link_text}' is present")
    
    @pytest.mark.regression
    def test_navigate_to_about_page(self, page):
        """Test navigation to About page"""
        logger.info("Testing navigation to About page")
        
        about_link = page.locator("#nav-about")
        about_link.click()
        page.wait_for_timeout(500)
        
        # Check if About page is active
        about_page = page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        logger.info("Successfully navigated to About page")
    
    @pytest.mark.regression
    def test_navigate_to_contact_page(self, page):
        """Test navigation to Contact page"""
        logger.info("Testing navigation to Contact page")
        
        contact_link = page.locator("#nav-contact")
        contact_link.click()
        page.wait_for_timeout(500)
        
        # Check if Contact page is active
        contact_page = page.locator("#page-contact")
        expect(contact_page).to_have_class("page active")
        logger.info("Successfully navigated to Contact page")
    
    @pytest.mark.regression
    def test_navigate_back_to_home(self, page):
        """Test navigation back to Home page"""
        logger.info("Testing navigation back to Home")
        
        # Go to About first
        page.locator("#nav-about").click()
        page.wait_for_timeout(300)
        
        # Navigate back to Home
        page.locator("#nav-home").click()
        page.wait_for_timeout(300)
        
        home_page = page.locator("#page-home")
        expect(home_page).to_have_class("page active")
        logger.info("Successfully navigated back to Home page")
    
    @pytest.mark.regression
    def test_active_nav_link_styling(self, page):
        """Test active navigation link gets correct styling"""
        logger.info("Testing active navigation link styling")
        
        # Home should be active by default
        home_link = page.locator("#nav-home")
        expect(home_link).to_have_class("active")
        
        # Click About
        page.locator("#nav-about").click()
        page.wait_for_timeout(300)
        
        # About should now be active, Home should not
        about_link = page.locator("#nav-about")
        expect(about_link).to_have_class("active")
        expect(home_link).not_to_have_class("active")
        
        logger.info("Active navigation styling works correctly")
    
    @pytest.mark.regression
    def test_logo_click_returns_home(self, page):
        """Test clicking logo returns to home page"""
        logger.info("Testing logo click navigation to home")
        
        # Navigate to About
        page.locator("#nav-about").click()
        page.wait_for_timeout(300)
        
        # Click logo
        page.locator(".nav-logo").click()
        page.wait_for_timeout(300)
        
        # Should be on home page
        home_page = page.locator("#page-home")
        expect(home_page).to_have_class("page active")
        logger.info("Logo click successfully returns to home")


class TestFooter:
    """Test footer functionality"""
    
    @pytest.mark.smoke
    def test_footer_logo_visible(self, page):
        """Test footer logo is visible"""
        logger.info("Testing footer logo visibility")
        footer_logo = page.locator("footer .footer-logo-wrap img")
        expect(footer_logo).to_be_visible()
        logger.info("Footer logo is visible")
    
    @pytest.mark.regression
    def test_footer_social_links(self, page):
        """Test footer social links are present"""
        logger.info("Testing footer social media links")
        
        # LinkedIn link
        linkedin = page.locator("footer a[href*='linkedin']")
        expect(linkedin).to_be_visible()
        logger.info("LinkedIn link is present in footer")
    
    @pytest.mark.regression
    def test_footer_contact_info(self, page):
        """Test footer contains contact information"""
        logger.info("Testing footer contact information")
        
        # Check for email
        email_link = page.locator("footer a[href='mailto:info@zanethembacleaning.co.za']")
        expect(email_link).to_be_visible()
        
        # Check for phone numbers
        phone1 = page.locator("footer a[href='tel:+27615460770']")
        expect(phone1).to_be_visible()
        
        logger.info("Footer contact information is complete")
    
    @pytest.mark.regression
    def test_footer_navigation_works(self, page):
        """Test footer navigation links work"""
        logger.info("Testing footer navigation functionality")
        
        # Find footer About Us link
        footer_about = page.locator("footer").get_by_text("About Us", exact=True)
        footer_about.click()
        page.wait_for_timeout(300)
        
        about_page = page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        logger.info("Footer navigation works correctly")


class TestMobileNavigation:
    """Test mobile navigation (hamburger menu)"""
    
    @pytest.mark.regression
    def test_hamburger_menu_visible_on_mobile(self, mobile_page):
        """Test hamburger menu is visible on mobile"""
        logger.info("Testing hamburger menu visibility on mobile")
        
        hamburger = mobile_page.locator("#hamburger")
        expect(hamburger).to_be_visible()
        logger.info("Hamburger menu is visible on mobile viewport")
    
    @pytest.mark.regression
    def test_hamburger_menu_opens(self, mobile_page):
        """Test hamburger menu opens when clicked"""
        logger.info("Testing hamburger menu opens")
        
        hamburger = mobile_page.locator("#hamburger")
        hamburger.click()
        mobile_page.wait_for_timeout(300)
        
        mobile_menu = mobile_page.locator("#mobileMenu")
        expect(mobile_menu).to_have_class("mobile-menu open")
        logger.info("Hamburger menu opens correctly")
    
    @pytest.mark.regression
    def test_mobile_menu_navigation(self, mobile_page):
        """Test navigation through mobile menu"""
        logger.info("Testing mobile menu navigation")
        
        # Open menu
        mobile_page.locator("#hamburger").click()
        mobile_page.wait_for_timeout(300)
        
        # Click About in mobile menu
        about_mobile = mobile_page.locator("#mob-about")
        about_mobile.click()
        mobile_page.wait_for_timeout(500)
        
        # Check About page is active
        about_page = mobile_page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        
        # Mobile menu should be closed
        mobile_menu = mobile_page.locator("#mobileMenu")
        expect(mobile_menu).not_to_have_class("mobile-menu open")
        
        logger.info("Mobile menu navigation works correctly")
    
    @pytest.mark.regression
    def test_hamburger_animates_when_open(self, mobile_page):
        """Test hamburger icon animates to X when open"""
        logger.info("Testing hamburger animation")
        
        hamburger = mobile_page.locator("#hamburger")
        
        # Initially not open
        expect(hamburger).not_to_have_class("hamburger open")
        
        # Click to open
        hamburger.click()
        mobile_page.wait_for_timeout(300)
        
        # Should have open class
        expect(hamburger).to_have_class("hamburger open")
        logger.info("Hamburger animates correctly")
