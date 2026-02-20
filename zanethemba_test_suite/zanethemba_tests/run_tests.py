#!/usr/bin/env python3
"""
Zanethemba Website Test Runner
Executes all tests and generates reports
"""
import subprocess
import sys
import os
from pathlib import Path

# Colors for terminal output (only for errors)
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def main():
    """Run tests and generate reports"""
    project_root = Path(__file__).parent
    os.chdir(project_root)
    
    print("=" * 80)
    print("ZANETHEMBA WEBSITE - TEST EXECUTION")
    print("=" * 80)
    print()
    
    # Check if playwright is installed
    print("Checking Playwright installation...")
    try:
        subprocess.run(
            ["python3", "-m", "playwright", "install", "chromium"],
            check=True,
            capture_output=True
        )
        print("✓ Playwright browsers ready")
    except subprocess.CalledProcessError as e:
        print(f"{RED}✗ Failed to install Playwright browsers{RESET}", file=sys.stderr)
        print(f"{RED}Error: {e.stderr.decode()}{RESET}", file=sys.stderr)
        return 1
    
    print()
    print("-" * 80)
    print("Running test suite...")
    print("-" * 80)
    print()
    
    # Run pytest with all options configured in pytest.ini
    # Logs go to file only (INFO level), only ERRORs to console
    result = subprocess.run(
        ["python3", "-m", "pytest"],
        cwd=project_root
    )
    
    print()
    print("=" * 80)
    
    if result.returncode == 0:
        print("✓ ALL TESTS PASSED")
    else:
        print(f"{RED}✗ SOME TESTS FAILED (exit code: {result.returncode}){RESET}", file=sys.stderr)
    
    print("=" * 80)
    print()
    
    # Report locations
    reports_dir = project_root / "reports"
    logs_dir = project_root / "logs"
    
    print("Reports generated:")
    print(f"  • HTML Report:     {reports_dir}/pytest_report.html")
    print(f"  • Coverage HTML:   {reports_dir}/coverage/index.html")
    print(f"  • JSON Results:    {reports_dir}/test_results.json")
    print(f"  • Coverage JSON:   {reports_dir}/coverage.json")
    print(f"  • Logs:            {logs_dir}/")
    print()
    print("View results in the dashboard:")
    print("  python3 dashboard/app.py")
    print("  Then open: http://localhost:5000")
    print()
    
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
