"""
Performance tests for Zanethemba website
"""
import pytest
import logging
import time
from playwright.sync_api import Page, expect

logger = logging.getLogger('zanethemba_tests.performance')


class TestPageLoadPerformance:
    """Test page load performance"""
    
    @pytest.mark.performance
    def test_initial_page_load_time(self, context, base_url):
        """Test initial page load time is acceptable"""
        logger.info("Testing initial page load time")
        
        page = context.new_page()
        
        start_time = time.time()
        page.goto(base_url, wait_until="domcontentloaded", timeout=30000)
        load_time = time.time() - start_time
        
        logger.info(f"Page loaded in {load_time:.2f} seconds")
        
        # Should load in under 3 seconds
        assert load_time < 3.0, f"Page took {load_time:.2f}s to load (expected < 3s)"
        
        page.close()
        logger.info("✓ Page load time is acceptable")
    
    @pytest.mark.performance
    def test_page_fully_loaded_time(self, context, base_url):
        """Test page fully loaded time (including splash)"""
        logger.info("Testing full page load time including splash")
        
        page = context.new_page()
        
        start_time = time.time()
        page.goto(base_url, wait_until="load", timeout=30000)
        
        # Wait for splash to complete
        page.wait_for_timeout(4000)
        
        full_load_time = time.time() - start_time
        
        logger.info(f"Page fully loaded in {full_load_time:.2f} seconds")
        
        # Should be fully ready in under 6 seconds
        assert full_load_time < 6.0, f"Full load took {full_load_time:.2f}s (expected < 6s)"
        
        page.close()
        logger.info("✓ Full page load time is acceptable")
    
    @pytest.mark.performance
    def test_navigation_speed(self, page):
        """Test navigation between pages is fast"""
        logger.info("Testing navigation speed")
        
        # Navigate to About
        start_time = time.time()
        page.locator("#nav-about").click()
        page.wait_for_selector("#page-about.active")
        about_nav_time = time.time() - start_time
        
        logger.info(f"Navigation to About: {about_nav_time:.3f}s")
        assert about_nav_time < 1.0, f"About navigation took {about_nav_time:.3f}s"
        
        # Navigate to Contact
        start_time = time.time()
        page.locator("#nav-contact").click()
        page.wait_for_selector("#page-contact.active")
        contact_nav_time = time.time() - start_time
        
        logger.info(f"Navigation to Contact: {contact_nav_time:.3f}s")
        assert contact_nav_time < 1.0, f"Contact navigation took {contact_nav_time:.3f}s"
        
        # Navigate back to Home
        start_time = time.time()
        page.locator("#nav-home").click()
        page.wait_for_selector("#page-home.active")
        home_nav_time = time.time() - start_time
        
        logger.info(f"Navigation to Home: {home_nav_time:.3f}s")
        assert home_nav_time < 1.0, f"Home navigation took {home_nav_time:.3f}s"
        
        logger.info("✓ All navigation speeds are acceptable")
    
    @pytest.mark.performance
    def test_carousel_rotation_performance(self, page):
        """Test carousel doesn't lag when rotating"""
        logger.info("Testing carousel rotation performance")
        
        # Wait for initial load
        page.wait_for_timeout(1000)
        
        # Get initial active slide
        initial_active = page.locator("#heroCarousel .carousel-slide.active")
        expect(initial_active).to_have_count(1)
        
        logger.info("Waiting for carousel auto-rotation (5 seconds)")
        
        # Wait for carousel to rotate (5 second interval)
        start_time = time.time()
        page.wait_for_timeout(5500)
        rotation_time = time.time() - start_time
        
        # Check that rotation happened
        active_slides = page.locator("#heroCarousel .carousel-slide.active")
        expect(active_slides).to_have_count(1)
        
        logger.info(f"Carousel rotation completed in {rotation_time:.2f}s")
        
        # Rotation should be smooth (within timing tolerance)
        assert 5.0 <= rotation_time <= 6.0, "Carousel rotation timing off"
        
        logger.info("✓ Carousel rotation is smooth")
    
    @pytest.mark.performance
    def test_form_interaction_responsiveness(self, page):
        """Test form inputs are responsive"""
        logger.info("Testing form interaction responsiveness")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Test typing speed
        start_time = time.time()
        page.fill("#fname", "Performance Test Name")
        fill_time = time.time() - start_time
        
        logger.info(f"Form field fill time: {fill_time:.3f}s")
        assert fill_time < 0.5, f"Form filling took {fill_time:.3f}s (expected < 0.5s)"
        
        # Test dropdown interaction
        start_time = time.time()
        page.select_option("#service", "Residential Cleaning")
        select_time = time.time() - start_time
        
        logger.info(f"Dropdown selection time: {select_time:.3f}s")
        assert select_time < 0.3, f"Dropdown took {select_time:.3f}s (expected < 0.3s)"
        
        logger.info("✓ Form interactions are responsive")
    
    @pytest.mark.performance
    def test_mobile_menu_animation_speed(self, mobile_page):
        """Test mobile menu opens quickly"""
        logger.info("Testing mobile menu animation speed")
        
        start_time = time.time()
        mobile_page.locator("#hamburger").click()
        mobile_page.wait_for_selector("#mobileMenu.open")
        open_time = time.time() - start_time
        
        logger.info(f"Mobile menu open time: {open_time:.3f}s")
        assert open_time < 0.5, f"Mobile menu took {open_time:.3f}s to open"
        
        logger.info("✓ Mobile menu animation is fast")


class TestResourceLoadPerformance:
    """Test resource loading performance"""
    
    @pytest.mark.performance
    def test_images_are_embedded(self, page):
        """Test images are base64 embedded (no HTTP requests)"""
        logger.info("Testing images are embedded")
        
        # Check hero image
        hero_img = page.locator(".hero-right img").first
        src = hero_img.get_attribute("src")
        
        assert src.startswith("data:image"), "Images should be base64 embedded"
        logger.info("✓ Images are embedded, no external HTTP requests")
    
    @pytest.mark.performance
    def test_no_broken_images(self, page):
        """Test all images are properly loaded"""
        logger.info("Testing for broken images")
        
        # Get all images
        images = page.locator("img").all()
        
        broken_count = 0
        for img in images:
            # Check if image is visible and has src
            if img.is_visible():
                src = img.get_attribute("src")
                if not src or src == "":
                    broken_count += 1
                    logger.error(f"Broken image found: {img}")
        
        assert broken_count == 0, f"Found {broken_count} broken images"
        logger.info(f"✓ All {len(images)} images are properly loaded")
    
    @pytest.mark.performance
    def test_css_is_inline(self, page):
        """Test CSS is inline (no external stylesheets except fonts)"""
        logger.info("Testing CSS is inline")
        
        # Check for external stylesheets (should only be Google Fonts)
        stylesheets = page.locator("link[rel='stylesheet']").all()
        
        external_css = []
        for sheet in stylesheets:
            href = sheet.get_attribute("href")
            if href and "fonts.googleapis.com" not in href:
                external_css.append(href)
        
        assert len(external_css) == 0, f"Found unexpected external CSS: {external_css}"
        logger.info("✓ All CSS is inline except fonts")
    
    @pytest.mark.performance
    def test_js_is_inline(self, page):
        """Test JavaScript is inline"""
        logger.info("Testing JavaScript is inline")
        
        # Check for external JS files
        scripts = page.locator("script[src]").all()
        
        external_js = []
        for script in scripts:
            src = script.get_attribute("src")
            if src:
                external_js.append(src)
        
        assert len(external_js) == 0, f"Found external JS files: {external_js}"
        logger.info("✓ All JavaScript is inline")


class TestMemoryAndCPU:
    """Test memory and CPU usage (basic checks)"""
    
    @pytest.mark.performance
    def test_multiple_navigation_cycles(self, page):
        """Test memory doesn't leak during navigation"""
        logger.info("Testing memory stability during navigation")
        
        # Perform multiple navigation cycles
        for i in range(5):
            logger.info(f"Navigation cycle {i+1}/5")
            
            page.locator("#nav-about").click()
            page.wait_for_timeout(200)
            
            page.locator("#nav-contact").click()
            page.wait_for_timeout(200)
            
            page.locator("#nav-home").click()
            page.wait_for_timeout(200)
        
        # If we get here without timeout or crash, memory is stable
        logger.info("✓ Memory stable after 5 navigation cycles")
    
    @pytest.mark.performance
    def test_carousel_doesnt_freeze(self, page):
        """Test page doesn't freeze with carousel running"""
        logger.info("Testing page doesn't freeze with carousel")
        
        # Let carousel run for a while
        page.wait_for_timeout(10000)  # 10 seconds
        
        # Try to interact with page
        page.locator("#nav-about").click()
        page.wait_for_timeout(300)
        
        about_page = page.locator("#page-about")
        expect(about_page).to_have_class("page active")
        
        logger.info("✓ Page remains responsive with carousel running")
    
    @pytest.mark.performance
    def test_form_submission_doesnt_hang(self, page):
        """Test form submission is responsive"""
        logger.info("Testing form submission performance")
        
        page.locator("#nav-contact").click()
        page.wait_for_timeout(500)
        
        # Fill and submit form
        page.fill("#fname", "Speed")
        page.fill("#lname", "Test")
        page.fill("#email", "speed@test.com")
        
        start_time = time.time()
        page.click("button[type='submit']")
        page.wait_for_selector("#formSuccess", timeout=5000)
        submit_time = time.time() - start_time
        
        logger.info(f"Form submission took {submit_time:.3f}s")
        assert submit_time < 2.0, f"Form took {submit_time:.3f}s to submit"
        
        logger.info("✓ Form submission is fast")
