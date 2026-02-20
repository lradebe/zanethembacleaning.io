"""
Test configuration and fixtures for Zanethemba website tests
"""
import os
import sys
import logging
import pytest
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext

# Set up project paths
PROJECT_ROOT = Path(__file__).parent
REPORTS_DIR = PROJECT_ROOT / "reports"
LOGS_DIR = PROJECT_ROOT / "logs"
WEBSITE_PATH = Path("/mnt/user-data/outputs/zanethemba_website.html")

# Create directories
REPORTS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# Configure logging - only ERROR to console, INFO+ to file
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler for all logs
log_file = LOGS_DIR / f"test_execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
file_handler = logging.FileHandler(log_file, mode='w')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Console handler only for errors
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.ERROR)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# Create test-specific logger
test_logger = logging.getLogger('zanethemba_tests')


@pytest.fixture(scope="session")
def base_url():
    """Return the base URL for the website"""
    if not WEBSITE_PATH.exists():
        test_logger.error(f"Website file not found at {WEBSITE_PATH}")
        pytest.fail(f"Website file not found: {WEBSITE_PATH}")
    
    url = f"file://{WEBSITE_PATH}"
    test_logger.info(f"Base URL configured: {url}")
    return url


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch arguments"""
    return {
        "headless": True,
        "args": ["--disable-dev-shm-usage"]
    }


@pytest.fixture(scope="session")
def playwright_instance():
    """Create a playwright instance for the session"""
    test_logger.info("Initializing Playwright")
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, browser_type_launch_args):
    """Create a browser instance"""
    test_logger.info("Launching browser")
    browser = playwright_instance.chromium.launch(**browser_type_launch_args)
    yield browser
    test_logger.info("Closing browser")
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    """Create a new browser context for each test"""
    test_logger.info("Creating new browser context")
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
    yield context
    test_logger.info("Closing browser context")
    context.close()


@pytest.fixture(scope="function")
def page(context, base_url):
    """Create a new page and navigate to base URL"""
    test_logger.info(f"Creating new page and navigating to {base_url}")
    page = context.new_page()
    page.goto(base_url, wait_until="domcontentloaded", timeout=30000)
    
    # Wait for splash screen to complete
    page.wait_for_timeout(4000)
    
    yield page
    test_logger.info("Closing page")
    page.close()


@pytest.fixture(scope="function")
def mobile_page(browser, base_url):
    """Create a mobile viewport page"""
    test_logger.info("Creating mobile viewport page")
    context = browser.new_context(
        viewport={"width": 375, "height": 667},
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)"
    )
    page = context.new_page()
    page.goto(base_url, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(4000)
    
    yield page
    
    page.close()
    context.close()
    test_logger.info("Closed mobile page and context")


@pytest.fixture(scope="function")
def tablet_page(browser, base_url):
    """Create a tablet viewport page"""
    test_logger.info("Creating tablet viewport page")
    context = browser.new_context(
        viewport={"width": 768, "height": 1024},
        user_agent="Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X)"
    )
    page = context.new_page()
    page.goto(base_url, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(4000)
    
    yield page
    
    page.close()
    context.close()
    test_logger.info("Closed tablet page and context")


def pytest_configure(config):
    """Configure pytest"""
    test_logger.info("=" * 80)
    test_logger.info("ZANETHEMBA WEBSITE TEST SUITE - STARTING")
    test_logger.info("=" * 80)


def pytest_unconfigure(config):
    """Cleanup after all tests"""
    test_logger.info("=" * 80)
    test_logger.info("ZANETHEMBA WEBSITE TEST SUITE - COMPLETED")
    test_logger.info("=" * 80)


def pytest_runtest_setup(item):
    """Log before each test"""
    test_logger.info(f"STARTING TEST: {item.nodeid}")


def pytest_runtest_teardown(item):
    """Log after each test"""
    test_logger.info(f"COMPLETED TEST: {item.nodeid}")


def pytest_runtest_logreport(report):
    """Log test results"""
    if report.when == "call":
        if report.passed:
            test_logger.info(f"✓ PASSED: {report.nodeid}")
        elif report.failed:
            test_logger.error(f"✗ FAILED: {report.nodeid}")
            test_logger.error(f"Error: {report.longreprtext}")
        elif report.skipped:
            test_logger.info(f"⊘ SKIPPED: {report.nodeid}")
