# 📥 DOWNLOAD & SETUP INSTRUCTIONS

## Download Options

Choose ONE of the following download options:

### Option 1: ZIP Archive (Recommended for Windows)
**File:** `zanethemba_test_suite.zip` (34 KB)
- Download the ZIP file
- Extract to your desired location
- Open terminal/command prompt in the extracted folder

### Option 2: TAR.GZ Archive (Recommended for Mac/Linux)
**File:** `zanethemba_test_suite.tar.gz` (24 KB)
- Download the TAR.GZ file
- Extract: `tar -xzf zanethemba_test_suite.tar.gz`
- Change directory: `cd zanethemba_tests`

## Quick Setup (After Download)

### Automatic Installation (Mac/Linux)
```bash
cd zanethemba_tests
chmod +x install.sh
./install.sh
```

### Manual Installation (All Platforms)
```bash
cd zanethemba_tests

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
python3 -m playwright install chromium
```

## Run Tests

```bash
# Run all tests
python3 run_tests.py

# View dashboard
python3 dashboard/app.py
# Then open: http://localhost:5000
```

## What's Included

After extraction, you'll have:
```
zanethemba_tests/
├── install.sh              # Automatic installation script
├── run_tests.py           # Test runner
├── QUICKSTART.md          # 5-minute guide
├── README.md              # Full documentation
├── requirements.txt       # Python dependencies
├── pytest.ini            # Test configuration
├── conftest.py           # Test fixtures
├── tests/                # 60+ test cases
│   ├── test_navigation.py
│   ├── test_content.py
│   ├── test_forms.py
│   ├── test_performance.py
│   └── test_negative.py
└── dashboard/            # Web dashboard
    ├── app.py
    └── templates/
```

## Requirements

- Python 3.8 or higher
- pip (Python package manager)
- Internet connection (for initial setup)
- ~200MB disk space (for Playwright browser)

## Troubleshooting

### "command not found: python3"
- Install Python from https://python.org
- Or try `python` instead of `python3`

### "pip: command not found"
- Install pip: `python3 -m ensurepip --upgrade`

### Permission denied on install.sh
- Run: `chmod +x install.sh`
- Then: `./install.sh`

### Playwright installation fails
- Try manually: `python3 -m playwright install chromium`
- Or with sudo: `sudo python3 -m playwright install chromium`

## Next Steps

1. Extract the downloaded archive
2. Run `install.sh` (or manual installation)
3. Run `python3 run_tests.py`
4. View results at `http://localhost:5000`

For detailed help, see `QUICKSTART.md` and `README.md` after extraction.

---

**Need Help?**
- Check QUICKSTART.md for step-by-step guide
- Review README.md for complete documentation
- All logs are in `logs/` directory after running tests
