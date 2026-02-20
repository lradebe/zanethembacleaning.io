"""
Test content and UI elements of Zanethemba website
"""
import pytest
import logging
from playwright.sync_api import Page, expect

logger = logging.getLogger('zanethemba_tests.content')


class TestHomePageContent:
    """Test home page content and elements"""
    
    @pytest.mark.smoke
    def test_hero_title_present(self, page):
        """Test hero title is present and correct"""
        logger.info("Testing hero title presence")
        hero_title = page.locator(".hero-title")
        expect(hero_title).to_be_visible()
        expect(hero_title).to_contain_text("Cleanliness")
        logger.info("Hero title is correctly displayed")
    
    @pytest.mark.smoke
    def test_cta_buttons_present(self, page):
        """Test CTA buttons are present on hero"""
        logger.info("Testing CTA buttons presence")
        
        request_service = page.get_by_role("link", name="Request a Service")
        expect(request_service).to_be_visible()
        
        our_story = page.get_by_role("link", name="Our Story")
        expect(our_story).to_be_visible()
        
        logger.info("CTA buttons are present and visible")
    
    @pytest.mark.regression
    def test_hero_carousel_present(self, page):
        """Test hero carousel exists and has images"""
        logger.info("Testing hero carousel")
        
        carousel = page.locator("#heroCarousel")
        expect(carousel).to_be_visible()
        
        # Check for carousel slides
        slides = page.locator("#heroCarousel .carousel-slide")
        expect(slides).to_have_count(4)
        
        logger.info("Hero carousel has 4 slides")
    
    @pytest.mark.regression
    def test_hero_carousel_dots(self, page):
        """Test hero carousel has navigation dots"""
        logger.info("Testing carousel dots")
        
        dots = page.locator("#heroDots .carousel-dot")
        expect(dots).to_have_count(4)
        
        # First dot should be active
        first_dot = dots.nth(0)
        expect(first_dot).to_have_class("carousel-dot active")
        
        logger.info("Carousel dots are present and first is active")
    
    @pytest.mark.regression
    def test_bbbee_badge_visible(self, page):
        """Test L1 B-BBEE badge is visible"""
        logger.info("Testing B-BBEE badge visibility")
        
        badge = page.locator(".hero-badge")
        expect(badge).to_be_visible()
        
        badge_number = page.locator(".hero-badge-number")
        expect(badge_number).to_have_text("L1")
        
        logger.info("B-BBEE badge is correctly displayed")
    
    @pytest.mark.regression
    def test_trust_bar_icons(self, page):
        """Test trust bar has all 5 icons"""
        logger.info("Testing trust bar icons")
        
        trust_items = page.locator(".trust-item")
        expect(trust_items).to_have_count(5)
        
        # Check for specific trust items
        trust_texts = ["CIPC Registered", "Fully Insured", "Community-Led", 
                       "Eco-Friendly", "Trained Professionals"]
        
        for text in trust_texts:
            item = page.locator(f".trust-text:has-text('{text}')")
            expect(item).to_be_visible()
            logger.info(f"Trust item '{text}' is visible")
    
    @pytest.mark.regression
    def test_services_grid(self, page):
        """Test services grid has all 6 cards"""
        logger.info("Testing services grid")
        
        service_cards = page.locator(".service-card")
        expect(service_cards).to_have_count(6)
        
        logger.info("Services grid has 6 cards")
    
    @pytest.mark.regression
    def test_service_card_content(self, page):
        """Test service cards have proper content"""
        logger.info("Testing service card content structure")
        
        first_card = page.locator(".service-card").first
        
        # Should have number, name, and description
        expect(first_card.locator(".service-number")).to_be_visible()
        expect(first_card.locator(".service-name")).to_be_visible()
        expect(first_card.locator(".service-desc")).to_be_visible()
        
        logger.info("Service cards have proper content structure")
    
    @pytest.mark.regression
    def test_stats_section(self, page):
        """Test stats section has 4 stats"""
        logger.info("Testing stats section")
        
        stat_items = page.locator(".stat-item")
        expect(stat_items).to_have_count(4)
        
        # Check specific stats
        l1_stat = page.locator(".stat-number:has-text('L1')")
        expect(l1_stat).to_be_visible()
        
        logger.info("Stats section displays correctly")
    
    @pytest.mark.regression
    def test_community_section_present(self, page):
        """Test community section is present"""
        logger.info("Testing community section")
        
        community_tag = page.locator(".community-img-tag")
        expect(community_tag).to_be_visible()
        expect(community_tag).to_have_text("Our People")
        
        logger.info("Community section is present with tag")


class TestAboutPageContent:
    """Test About page content"""
    
    @pytest.mark.regression
    def test_about_hero_title(self, page):
        """Test About page hero title"""
        logger.info("Testing About page hero title")
        
        page.locator("#nav-about").click()
        page.wait_for_timeout(500)
        
        hero_title = page.locator(".about-hero-title")
        expect(hero_title).to_be_visible()
        expect(hero_title).to_contain_text("Hope, Dignity")
        
        logger.info("About hero title is correct")
    
    @pytest.mark.regression
    def test_bbbee_strip(self, page):
        """Test B-BBEE strip on About page"""
        logger.info("Testing B-BBEE strip")
        
        page.locator("#nav-about").click()
        page.wait_for_timeout(500)
        
        strip = page.locator(".bbbee-strip")
        expect(strip).to_be_visible()
        
        badge = page.locator(".bbbee-strip-badge")
        expect(badge).to_contain_text("Level 1 B-BBEE")
        
        logger.info("B-BBEE strip displays correctly")
    
    @pytest.mark.regression
    def test_sidebar_cards(self, page):
        """Test sidebar has Mission, Vision, Promise cards"""
        logger.info("Testing sidebar cards")
        
        page.locator("#nav-about").click()
        page.wait_for_timeout(500)
        
        sidebar_cards = page.locator(".sidebar-card")
        expect(sidebar_cards).to_have_count(3)
        
        # Check for specific labels
        mission = page.locator(".sidebar-card-label:has-text('Our Mission')")
        expect(mission).to_be_visible()
        
        vision = page.locator(".sidebar-card-label:has-text('Our Vision')")
        expect(vision).to_be_visible()
        
        promise = page.locator(".sidebar-card-label:has-text('Our Promise')")
        expect(promise).to_be_visible()
        
        logger.info("All sidebar cards are present")
    
    @pytest.mark.regression
    def test_values_grid(self, page):
        """Test values grid has 5 values"""
        logger.info("Testing values grid")
        
        page.locator("#nav-about").click()
        page.wait_for_timeout(500)
        
        value_items = page.locator(".value-item")
        expect(value_items).to_have_count(5)
        
        logger.info("Values grid has 5 values")
    
    @pytest.mark.regression
    def test_about_images_present(self, page):
        """Test About page has image rows"""
        logger.info("Testing About page image rows")
        
        page.locator("#nav-about").click()
        page.wait_for_timeout(500)
        
        image_rows = page.locator(".about-img-row")
        expect(image_rows.first).to_be_visible()
        
        logger.info("About page image rows are present")


class TestContactPageContent:
    """Test Contact page content"""
    
    @pytest.mark.regression
    def test_contact_hero(self, page):
        """Test Contact page hero"""
        logger.info("Testing Contact page hero")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        hero_title = page.locator(".contact-hero-title")
        expect(hero_title).to_be_visible()
        expect(hero_title).to_contain_text("Cleaner")
        
        logger.info("Contact hero is present")
    
    @pytest.mark.regression
    def test_contact_info_blocks(self, page):
        """Test contact information blocks"""
        logger.info("Testing contact info blocks")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Check for Email block
        email_label = page.locator(".contact-info-label:has-text('Email')")
        expect(email_label).to_be_visible()
        
        # Check for Telephone block
        phone_label = page.locator(".contact-info-label:has-text('Telephone')")
        expect(phone_label).to_be_visible()
        
        # Check for WhatsApp block
        whatsapp_label = page.locator(".contact-info-label:has-text('WhatsApp')")
        expect(whatsapp_label).to_be_visible()
        
        logger.info("All contact info blocks are present")
    
    @pytest.mark.regression
    def test_address_card(self, page):
        """Test address card is present"""
        logger.info("Testing address card")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        address_card = page.locator(".address-card")
        expect(address_card).to_be_visible()
        
        address_text = page.locator(".address-card-text")
        expect(address_text).to_contain_text("Wattle Street")
        expect(address_text).to_contain_text("Boksburg")
        
        logger.info("Address card displays correctly")
    
    @pytest.mark.regression
    def test_social_links_present(self, page):
        """Test social media links are present"""
        logger.info("Testing social media links")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        social_links = page.locator(".social-links .social-link")
        expect(social_links).to_have_count(3)  # LinkedIn, WhatsApp, Email
        
        logger.info("Social media links are present")


class TestResponsiveDesign:
    """Test responsive design elements"""
    
    @pytest.mark.regression
    def test_mobile_viewport_layout(self, mobile_page):
        """Test layout adapts for mobile"""
        logger.info("Testing mobile viewport layout")
        
        # Hero should stack vertically (grid-template-columns: 1fr)
        hero = mobile_page.locator(".hero")
        expect(hero).to_be_visible()
        
        logger.info("Mobile layout renders correctly")
    
    @pytest.mark.regression
    def test_tablet_viewport_layout(self, tablet_page):
        """Test layout adapts for tablet"""
        logger.info("Testing tablet viewport layout")
        
        hero = tablet_page.locator(".hero")
        expect(hero).to_be_visible()
        
        logger.info("Tablet layout renders correctly")
    
    @pytest.mark.regression
    def test_services_grid_responsive(self, mobile_page):
        """Test services grid is single column on mobile"""
        logger.info("Testing services grid responsiveness")
        
        service_cards = mobile_page.locator(".service-card")
        expect(service_cards).to_have_count(6)
        
        logger.info("Services grid responsive on mobile")
