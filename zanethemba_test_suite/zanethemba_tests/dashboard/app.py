"""
Zanethemba Test Dashboard
Flask application to display test results, coverage, and logs
"""
from flask import Flask, render_template, jsonify, send_from_directory
import json
import os
from pathlib import Path
from datetime import datetime
import glob

app = Flask(__name__)

# Paths
BASE_DIR = Path(__file__).parent.parent
REPORTS_DIR = BASE_DIR / "reports"
LOGS_DIR = BASE_DIR / "logs"


def get_latest_file(directory, pattern):
    """Get the most recent file matching pattern"""
    files = glob.glob(str(directory / pattern))
    if not files:
        return None
    return max(files, key=os.path.getctime)


def parse_log_file(log_path):
    """Parse log file into structured data"""
    if not log_path or not os.path.exists(log_path):
        return []
    
    logs = []
    with open(log_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            # Parse log format: YYYY-MM-DD HH:MM:SS [LEVEL] name - message
            try:
                parts = line.split(' ', 3)
                if len(parts) >= 4:
                    date = parts[0]
                    time = parts[1]
                    level_part = parts[2]
                    message = parts[3] if len(parts) > 3 else ""
                    
                    # Extract level from [LEVEL]
                    level = level_part.strip('[]')
                    
                    logs.append({
                        'timestamp': f"{date} {time}",
                        'level': level,
                        'message': message
                    })
            except:
                # If parsing fails, add as raw message
                logs.append({
                    'timestamp': '',
                    'level': 'INFO',
                    'message': line
                })
    
    return logs


def get_test_summary():
    """Get test summary from JSON report"""
    json_report = REPORTS_DIR / "test_results.json"
    
    if not json_report.exists():
        return {
            'total': 0,
            'passed': 0,
            'failed': 0,
            'skipped': 0,
            'duration': 0,
            'tests': []
        }
    
    with open(json_report, 'r') as f:
        data = json.load(f)
    
    summary = data.get('summary', {})
    tests = data.get('tests', [])
    
    return {
        'total': summary.get('total', 0),
        'passed': summary.get('passed', 0),
        'failed': summary.get('failed', 0),
        'skipped': summary.get('skipped', 0),
        'duration': summary.get('duration', 0),
        'tests': tests
    }


def get_coverage_data():
    """Get coverage data from JSON report"""
    coverage_json = REPORTS_DIR / "coverage.json"
    
    if not coverage_json.exists():
        return {
            'percent': 0,
            'covered': 0,
            'total': 0,
            'files': []
        }
    
    with open(coverage_json, 'r') as f:
        data = json.load(f)
    
    totals = data.get('totals', {})
    files = data.get('files', {})
    
    return {
        'percent': totals.get('percent_covered', 0),
        'covered': totals.get('covered_lines', 0),
        'total': totals.get('num_statements', 0),
        'files': files
    }


@app.route('/')
def index():
    """Dashboard home page"""
    summary = get_test_summary()
    coverage = get_coverage_data()
    
    # Get latest log file
    latest_log = get_latest_file(LOGS_DIR, "*.log")
    log_name = os.path.basename(latest_log) if latest_log else "No logs available"
    
    return render_template('index.html', 
                         test_summary=summary,
                         coverage=coverage,
                         log_file=log_name,
                         current_page='home')


@app.route('/tests')
def tests_page():
    """Test cases detail page"""
    summary = get_test_summary()
    return render_template('tests.html', 
                         tests=summary['tests'],
                         summary=summary,
                         current_page='tests')


@app.route('/coverage')
def coverage_page():
    """Coverage report page"""
    coverage = get_coverage_data()
    return render_template('coverage.html', 
                         coverage=coverage,
                         current_page='coverage')


@app.route('/logs')
def logs_page():
    """Logs viewer page"""
    latest_log = get_latest_file(LOGS_DIR, "*.log")
    logs = parse_log_file(latest_log)
    
    # Separate by level
    info_logs = [l for l in logs if l['level'] == 'INFO']
    error_logs = [l for l in logs if l['level'] == 'ERROR']
    
    return render_template('logs.html', 
                         all_logs=logs,
                         info_logs=info_logs,
                         error_logs=error_logs,
                         log_file=os.path.basename(latest_log) if latest_log else "None",
                         current_page='logs')


@app.route('/api/logs')
def api_logs():
    """API endpoint for logs"""
    latest_log = get_latest_file(LOGS_DIR, "*.log")
    logs = parse_log_file(latest_log)
    return jsonify(logs)


@app.route('/api/tests')
def api_tests():
    """API endpoint for test results"""
    summary = get_test_summary()
    return jsonify(summary)


@app.route('/api/coverage')
def api_coverage():
    """API endpoint for coverage data"""
    coverage = get_coverage_data()
    return jsonify(coverage)


@app.route('/reports/<path:filename>')
def serve_report(filename):
    """Serve static report files"""
    return send_from_directory(REPORTS_DIR, filename)


if __name__ == '__main__':
    print("=" * 80)
    print("ZANETHEMBA TEST DASHBOARD")
    print("=" * 80)
    print(f"Reports directory: {REPORTS_DIR}")
    print(f"Logs directory: {LOGS_DIR}")
    print("")
    print("Starting dashboard server at http://localhost:5000")
    print("=" * 80)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
