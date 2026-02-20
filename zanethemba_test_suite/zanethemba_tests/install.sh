#!/bin/bash
# Zanethemba Test Suite - Installation Script

echo "================================================================================"
echo "ZANETHEMBA TEST SUITE - INSTALLATION"
echo "================================================================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed"
echo ""

# Install Playwright browsers
echo "Installing Playwright browsers (this may take a minute)..."
python3 -m playwright install chromium

if [ $? -ne 0 ]; then
    echo "❌ Failed to install Playwright browsers"
    exit 1
fi

echo "✓ Playwright browsers installed"
echo ""

# Create directories
mkdir -p reports logs

echo "================================================================================"
echo "✓ INSTALLATION COMPLETE!"
echo "================================================================================"
echo ""
echo "Next steps:"
echo ""
echo "  1. Run tests:"
echo "     python3 run_tests.py"
echo ""
echo "  2. View dashboard:"
echo "     python3 dashboard/app.py"
echo "     Then open: http://localhost:5000"
echo ""
echo "For more information, see:"
echo "  • QUICKSTART.md - 5-minute guide"
echo "  • README.md - Complete documentation"
echo ""
