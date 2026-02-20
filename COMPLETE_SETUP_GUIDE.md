# 🎉 COMPLETE SETUP GUIDE - Zanethemba Test Suite

## 📥 Step 1: Download Files (Choose ONE option)

### Option A: Download ZIP File (Easiest - 34 KB)
1. Download **zanethemba_test_suite.zip**
2. Extract the ZIP file
3. You'll get a folder called `zanethemba_tests`

### Option B: Download TAR.GZ File (Smaller - 24 KB)
1. Download **zanethemba_test_suite.tar.gz**
2. Extract: `tar -xzf zanethemba_test_suite.tar.gz`
3. You'll get a folder called `zanethemba_tests`

## 📄 Step 2: Download the Website File

**Also download:** `zanethemba_website.html` (3.5 MB)

This is the website that the tests will run against.

## 📂 Step 3: Organize Your Files

Create a folder structure like this:

```
my-project-folder/
├── zanethemba_website.html          ← Website file
└── zanethemba_tests/                ← Extracted test suite
    ├── install.sh
    ├── run_tests.py
    ├── QUICKSTART.md
    ├── README.md
    ├── requirements.txt
    ├── tests/
    └── dashboard/
```

**IMPORTANT:** The test suite expects the website file to be at:
`/mnt/user-data/outputs/zanethemba_website.html`

If you're running tests locally, you'll need to update the path in `conftest.py`:

```python
# Find this line in conftest.py (around line 12):
WEBSITE_PATH = Path("/mnt/user-data/outputs/zanethemba_website.html")

# Change it to your local path:
WEBSITE_PATH = Path("../zanethemba_website.html")  # Or absolute path
```

## 🚀 Step 4: Install & Run

### Automatic Installation (Mac/Linux)
```bash
cd zanethemba_tests
chmod +x install.sh
./install.sh
```

### Manual Installation (Windows/All Platforms)
```bash
cd zanethemba_tests

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browser
python -m playwright install chromium
```

## ▶️ Step 5: Run Tests

```bash
# Make sure you're in the zanethemba_tests folder
python run_tests.py
```

**Expected Output:**
```
================================================================================
ZANETHEMBA WEBSITE - TEST EXECUTION
================================================================================

Checking Playwright installation...
✓ Playwright browsers ready

--------------------------------------------------------------------------------
Running test suite...
--------------------------------------------------------------------------------

tests/test_navigation.py ........
tests/test_content.py ....................
tests/test_forms.py ...............
tests/test_performance.py ..........
tests/test_negative.py ....................

================================================================================
✓ ALL TESTS PASSED
================================================================================

Reports generated:
  • HTML Report:     reports/pytest_report.html
  • Coverage HTML:   reports/coverage/index.html
  • JSON Results:    reports/test_results.json
  • Logs:            logs/
```

## 📊 Step 6: View Dashboard

```bash
# Start the dashboard (from zanethemba_tests folder)
python dashboard/app.py
```

Then open your browser to: **http://localhost:5000**

You'll see:
- 📈 **Overview** - Test summary and coverage stats
- ✅ **Test Cases** - All 60+ tests with status
- 📊 **Coverage** - Code coverage reports
- 📝 **Logs** - Complete execution logs (INFO + ERROR)

## 📁 What Each File Does

### Downloaded Files:

1. **zanethemba_test_suite.zip** or **.tar.gz**
   - Complete test suite in compressed format
   - Extract this to get started

2. **zanethemba_website.html**
   - The website being tested
   - Must be accessible to the test suite

3. **DOWNLOAD_INSTRUCTIONS.md**
   - Quick download guide (this file!)

4. **TEST_SUITE_OVERVIEW.md**
   - Detailed overview of test suite features

### Files After Extraction:

- **install.sh** - Automatic installation script
- **run_tests.py** - Main test runner
- **QUICKSTART.md** - 5-minute quick start guide
- **README.md** - Complete documentation
- **pytest.ini** - Test configuration
- **conftest.py** - Test fixtures and logging
- **requirements.txt** - Python dependencies
- **tests/** - All test files (60+ tests)
- **dashboard/** - Web dashboard application

### Generated After Running Tests:

- **reports/** - Test and coverage reports
  - pytest_report.html
  - coverage/index.html
  - test_results.json
  - coverage.json

- **logs/** - Execution logs
  - test_execution_YYYYMMDD_HHMMSS.log

## 🎯 Quick Commands

```bash
# Run all tests
python run_tests.py

# Run only smoke tests (fastest)
python -m pytest -m smoke

# Run only performance tests
python -m pytest -m performance

# Run specific test file
python -m pytest tests/test_navigation.py

# View latest log
cat logs/test_execution_*.log

# Start dashboard
python dashboard/app.py
```

## ✅ Success Checklist

After setup, you should have:
- ✅ Python 3.8+ installed
- ✅ All dependencies installed (from requirements.txt)
- ✅ Playwright browser installed
- ✅ Test suite extracted
- ✅ Website HTML file accessible
- ✅ Tests run successfully
- ✅ Dashboard accessible at localhost:5000

## 🔧 Troubleshooting

### "ModuleNotFoundError: No module named 'playwright'"
```bash
pip install playwright
python -m playwright install chromium
```

### "Website file not found"
Update the path in `conftest.py`:
```python
WEBSITE_PATH = Path("path/to/your/zanethemba_website.html")
```

### "Permission denied: install.sh"
```bash
chmod +x install.sh
./install.sh
```

### Dashboard won't start
Make sure you ran tests first:
```bash
python run_tests.py
python dashboard/app.py
```

### No reports generated
Check if tests ran successfully:
```bash
ls reports/  # Should show HTML and JSON files
ls logs/     # Should show log files
```

## 📚 Documentation

After extraction, read these files in order:

1. **QUICKSTART.md** - Get started in 5 minutes
2. **README.md** - Complete reference guide
3. Test the dashboard at http://localhost:5000

## 🎨 Dashboard Features

The dashboard is styled to match Zanethemba's branding:
- Crimson red (#8B1A1A) for accents
- Green (#4A7C2F) for success states
- Cream (#FDFCF8) background
- Cormorant Garamond + DM Sans fonts

### Dashboard Pages:

1. **Overview (/)** - Summary stats and quick links
2. **Test Cases (/tests)** - All tests with filtering
3. **Coverage (/coverage)** - Code coverage reports
4. **Logs (/logs)** - Complete execution logs

## 🎉 You're All Set!

Follow the steps above and you'll have:
- ✅ 60+ automated tests running
- ✅ Beautiful dashboard with all results
- ✅ Complete logs (INFO + ERROR)
- ✅ Coverage reports
- ✅ Professional test infrastructure

**Questions?**
- Check QUICKSTART.md for quick help
- Read README.md for detailed docs
- View logs in the dashboard

---

**Zanethemba Cleaning Services (Pty) Ltd**  
*"Bringing Hope Through Cleanliness"*
