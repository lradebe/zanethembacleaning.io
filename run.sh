#!/bin/bash
# Zanethemba Flask - Run Script

echo "Starting Zanethemba Cleaning Services..."
echo "========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the application
echo ""
echo "Starting Flask application..."
echo "Access at: http://localhost:5000"
echo "Press CTRL+C to stop"
echo ""

python app.py
