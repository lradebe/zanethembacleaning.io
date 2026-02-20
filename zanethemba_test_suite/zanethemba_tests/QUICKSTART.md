# Zanethemba Test Suite - Quick Start Guide

## 🚀 Installation & Setup (5 minutes)

### Step 1: Install Dependencies
```bash
cd zanethemba_tests
pip install -r requirements.txt
```

### Step 2: Install Playwright Browsers
```bash
python3 -m playwright install chromium
```

## ▶️ Running Tests (2 minutes)

### Run All Tests
```bash
python3 run_tests.py
```

This will:
- ✅ Execute all test cases (~60-80 tests)
- 📊 Generate coverage reports
- 📝 Create detailed logs
- ⏱️ Complete in ~30-60 seconds

### Expected Output
```
===============================================================================
ZANETHEMBA WEBSITE - TEST EXECUTION
===============================================================================

Checking Playwright installation...
✓ Playwright browsers ready

-------------------------------------------------------------------------------
Running test suite...
-------------------------------------------------------------------------------

tests/test_navigation.py::TestNavigation::test_splash_screen_appears PASSED
tests/test_navigation.py::TestNavigation::test_logo_visible_in_nav PASSED
... (more tests)

===============================================================================
✓ ALL TESTS PASSED
===============================================================================

Reports generated:
  • HTML Report:     reports/pytest_report.html
  • Coverage HTML:   reports/coverage/index.html
  • JSON Results:    reports/test_results.json
  • Coverage JSON:   reports/coverage.json
  • Logs:            logs/
```

## 📊 View Dashboard (30 seconds)

### Step 1: Start Dashboard Server
```bash
python3 dashboard/app.py
```

### Step 2: Open Browser
Navigate to: **http://localhost:5000**

You'll see:
- 📈 Overview page with stats
- ✅ Test cases with pass/fail status  
- 📊 Coverage reports
- 📝 Complete logs (INFO & ERROR)

## 🎯 Quick Commands

```bash
# Run only smoke tests (fastest)
pytest -m smoke

# Run only performance tests
pytest -m performance

# Run only negative tests
pytest -m negative

# Run specific test file
pytest tests/test_navigation.py

# View latest log
cat logs/test_execution_*.log
```

## ✅ What to Expect

### Test Results
- **Total Tests:** ~60-80
- **Expected Pass Rate:** 95-100%
- **Execution Time:** 30-60 seconds
- **Coverage:** 60-80% (higher with application code)

### Reports Generated
1. `reports/pytest_report.html` - Full test report
2. `reports/coverage/index.html` - Line-by-line coverage
3. `reports/test_results.json` - Machine-readable results
4. `logs/test_execution_YYYYMMDD_HHMMSS.log` - Complete logs

### Log Behavior
- ⚠️ **Console:** Only shows ERROR logs
- ✅ **File:** Contains both INFO and ERROR logs
- 📊 **Dashboard:** Shows all logs with filtering

## 🎨 Dashboard Features

### 1. Overview (`/`)
Quick stats and health check

### 2. Test Cases (`/tests`)
- All test results
- Filter by status
- See execution times

### 3. Coverage (`/coverage`)
- Overall coverage %
- File-by-file breakdown
- Link to detailed HTML report

### 4. Logs (`/logs`)
- All log entries
- Filter by INFO/ERROR
- Timestamped entries

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'playwright'"
```bash
pip install playwright
python3 -m playwright install chromium
```

### "Website file not found"
Check that `/mnt/user-data/outputs/zanethemba_website.html` exists

### No logs appearing
Logs are in `logs/` directory - check there instead of console

### Dashboard shows 0 tests
Run tests first with `python3 run_tests.py`, then start dashboard

## 📚 More Information

See `README.md` for:
- Detailed test descriptions
- Configuration options
- Advanced usage
- Contributing guidelines

---

**Need Help?**
- Check `logs/test_execution_*.log` for detailed execution logs
- Review `reports/pytest_report.html` for visual test results
- See `README.md` for comprehensive documentation
