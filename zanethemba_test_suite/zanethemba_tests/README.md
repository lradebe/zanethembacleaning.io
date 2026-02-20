# Zanethemba Website - Automated Test Suite

Comprehensive automated testing suite for the Zanethemba Cleaning Services website using Pytest and Playwright.

## 📋 Overview

This test suite provides:
- ✅ **Happy Path Tests** - Core functionality and user flows
- ❌ **Negative Tests** - Edge cases, invalid inputs, error handling
- ⚡ **Performance Tests** - Load times, navigation speed, carousel performance
- 📊 **Code Coverage** - Detailed coverage reports with visual dashboard
- 📝 **Structured Logging** - INFO and ERROR level logs (console shows only errors)
- 🎨 **Visual Dashboard** - Beautiful web interface matching Zanethemba's styling

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
python3 -m playwright install chromium
```

### Running Tests

```bash
# Run all tests
python3 run_tests.py

# Or use pytest directly
python3 -m pytest
```

### View Dashboard

```bash
# Start the dashboard server
python3 dashboard/app.py

# Open in browser
# http://localhost:5000
```

## 📁 Project Structure

```
zanethemba_tests/
├── tests/
│   ├── test_navigation.py    # Navigation & UI tests
│   ├── test_content.py        # Content & element tests
│   ├── test_forms.py          # Form & interaction tests
│   ├── test_performance.py    # Performance benchmarks
│   └── test_negative.py       # Negative/edge case tests
├── dashboard/
│   ├── app.py                 # Flask dashboard app
│   ├── templates/             # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── tests.html
│   │   ├── coverage.html
│   │   └── logs.html
│   └── static/                # Static assets
├── reports/
│   ├── pytest_report.html     # HTML test report
│   ├── coverage/              # Coverage HTML report
│   ├── test_results.json      # Test results JSON
│   └── coverage.json          # Coverage JSON
├── logs/
│   └── test_execution_*.log   # Timestamped log files
├── conftest.py                # Pytest configuration
├── pytest.ini                 # Pytest settings
├── requirements.txt           # Dependencies
├── run_tests.py              # Test runner script
└── README.md                  # This file
```

## 🧪 Test Categories

### Navigation Tests (`test_navigation.py`)
- Splash screen behavior
- Navigation links functionality
- Logo and brand name display
- Active link styling
- Mobile hamburger menu
- Footer navigation

**Markers:** `@pytest.mark.smoke`, `@pytest.mark.regression`

### Content Tests (`test_content.py`)
- Hero section content
- CTA buttons
- Carousel functionality
- Trust bar icons
- Services grid
- Stats section
- B-BBEE badges
- Responsive design

**Markers:** `@pytest.mark.smoke`, `@pytest.mark.regression`

### Form Tests (`test_forms.py`)
- Contact form validation
- Required field enforcement
- Email format validation
- Form submission
- CTA button navigation
- External link protocols

**Markers:** `@pytest.mark.smoke`, `@pytest.mark.regression`, `@pytest.mark.negative`

### Performance Tests (`test_performance.py`)
- Initial page load time (< 3s target)
- Full page load time (< 6s with splash)
- Navigation speed (< 1s target)
- Carousel rotation smoothness
- Form interaction responsiveness
- Mobile menu animation speed
- Resource loading (embedded images)
- Memory stability

**Markers:** `@pytest.mark.performance`

### Negative Tests (`test_negative.py`)
- Invalid email format
- Empty form submission
- Extremely long inputs
- Special characters & XSS attempts
- SQL injection attempts
- Rapid navigation clicks
- Double-click handling
- Mobile edge cases
- Carousel edge cases
- Browser compatibility

**Markers:** `@pytest.mark.negative`

## 📊 Dashboard Features

### Overview Page
- Test execution summary (total, passed, failed)
- Coverage percentage with progress bar
- Duration statistics
- Quick links to detailed views

### Test Cases Page
- Complete list of all test cases
- Pass/fail status with badges
- Execution duration per test
- Filterable by status (All, Passed, Failed, Skipped)

### Coverage Page
- Overall coverage percentage
- Covered vs total lines
- File-by-file breakdown
- Link to detailed HTML coverage report

### Logs Page
- All INFO and ERROR logs
- Timestamped entries
- Filterable by level
- Searchable log viewer

## 🎨 Dashboard Styling

The dashboard matches Zanethemba's brand identity:
- **Colors:** Crimson red (#8B1A1A), Green (#4A7C2F), Cream (#FDFCF8)
- **Typography:** Cormorant Garamond (headings), DM Sans (body)
- **Design:** Clean, professional, consistent with main website

## 📝 Logging

### Log Levels
- **INFO:** Test execution flow, navigation events, assertions
- **ERROR:** Test failures, exceptions, critical issues

### Console Output
- ❌ **Errors only** - Only ERROR level logs appear in terminal
- ✅ **Success indicators** - Pass/fail summary at end
- 📊 **Report locations** - Paths to generated reports

### Log Files
- 📂 **Location:** `logs/test_execution_YYYYMMDD_HHMMSS.log`
- 📄 **Format:** `YYYY-MM-DD HH:MM:SS [LEVEL] module - message`
- 💾 **Retention:** All INFO and ERROR logs saved to file

## 🔧 Configuration

### pytest.ini
- Test discovery patterns
- Coverage settings
- Report generation
- Log file configuration
- Pytest markers

### conftest.py
- Browser fixtures (desktop, mobile, tablet)
- Logging configuration
- Test lifecycle hooks
- Custom fixtures

## 📈 Coverage Reporting

Multiple coverage report formats:
- **HTML:** Interactive line-by-line coverage (`reports/coverage/index.html`)
- **JSON:** Machine-readable data (`reports/coverage.json`)
- **Terminal:** Summary in console (only if errors)

## 🎯 Test Execution Options

```bash
# Run specific test file
pytest tests/test_navigation.py

# Run tests by marker
pytest -m smoke                # Quick smoke tests
pytest -m regression          # Full regression suite
pytest -m performance         # Performance tests only
pytest -m negative           # Negative tests only

# Run with verbose output (errors only to console)
pytest -v

# Run specific test
pytest tests/test_forms.py::TestContactForm::test_form_submission_happy_path

# Run in parallel (install pytest-xdist first)
pytest -n auto
```

## 🐛 Debugging

### View detailed logs
```bash
# View latest log file
cat logs/test_execution_*.log | tail -100

# Filter ERROR logs only
grep ERROR logs/test_execution_*.log

# Real-time log following
tail -f logs/test_execution_*.log
```

### Run tests in headed mode (see browser)
Edit `conftest.py` and change `headless: True` to `headless: False`

### Generate trace for failed tests
```bash
pytest --tracing retain-on-failure
```

## 📚 Dependencies

- **pytest** - Testing framework
- **playwright** - Browser automation
- **pytest-playwright** - Playwright integration
- **pytest-cov** - Coverage plugin
- **pytest-html** - HTML reports
- **pytest-json-report** - JSON reports
- **flask** - Dashboard web server
- **jinja2** - Template engine

## ✅ Success Criteria

A successful test run meets:
- ✓ All smoke tests pass
- ✓ 95%+ regression tests pass
- ✓ No performance tests fail
- ✓ Page load < 3 seconds
- ✓ Navigation < 1 second
- ✓ Code coverage > 80% (if applicable)
- ✓ No ERROR logs (except expected negative test errors)

## 🤝 Contributing

When adding new tests:
1. Place in appropriate test file by category
2. Add proper `@pytest.mark` decorators
3. Include INFO logging for test flow
4. Use ERROR logging for failures
5. Follow existing naming conventions
6. Update this README if adding new categories

## 📞 Support

For issues or questions about the test suite:
- Review logs in `logs/` directory
- Check dashboard at http://localhost:5000
- Review pytest.ini configuration
- Examine conftest.py fixtures

---

**Zanethemba Cleaning Services (Pty) Ltd**  
*"Bringing Hope Through Cleanliness"*
