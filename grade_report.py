import json
import os

def safe_load_json(filename):
    """Safely load JSON file with error handling"""
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found")
        return None
    
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading {filename}: {e}")
        return None

def extract_test_results(json_data):
    """Extract passed/total from pytest JSON report"""
    if not json_data:
        return 0, 0
    
    # Try different possible structures
    summary = json_data.get('summary', {})
    
    # pytest-json-report format
    if 'passed' in summary and 'total' in summary:
        return summary['passed'], summary['total']
    
    # Alternative format - count from tests array
    tests = json_data.get('tests', [])
    if tests:
        passed = sum(1 for test in tests if test.get('outcome') == 'passed')
        total = len(tests)
        return passed, total
    
    # Fallback - look for other common keys
    passed = summary.get('passed', summary.get('num_passed', 0))
    failed = summary.get('failed', summary.get('num_failed', 0))
    error = summary.get('error', summary.get('num_error', 0))
    skipped = summary.get('skipped', summary.get('num_skipped', 0))
    
    total = passed + failed + error + skipped
    if total == 0:
        total = summary.get('total', summary.get('collected', 0))
    
    return passed, total

def calculate_grade():
    total_score = 0
    max_score = 100
    
    # Debug: Print current directory and files
    print("Current directory:", os.getcwd())
    print("Files in directory:", os.listdir('.'))
    
    # Basic tests (25 points)
    basic_data = safe_load_json('basic_results.json')
    basic_passed, basic_total = extract_test_results(basic_data)
    basic_score = (basic_passed / basic_total) * 25 if basic_total > 0 else 0
    
    print(f"Basic tests: {basic_passed}/{basic_total} = {basic_score:.1f}/25")
    
    # Intermediate tests (35 points)
    intermediate_data = safe_load_json('intermediate_results.json')
    intermediate_passed, intermediate_total = extract_test_results(intermediate_data)
    intermediate_score = (intermediate_passed / intermediate_total) * 35 if intermediate_total > 0 else 0
    
    print(f"Intermediate tests: {intermediate_passed}/{intermediate_total} = {intermediate_score:.1f}/35")
    
    # Advanced tests (40 points)
    advanced_data = safe_load_json('advanced_results.json')
    advanced_passed, advanced_total = extract_test_results(advanced_data)
    advanced_score = (advanced_passed / advanced_total) * 40 if advanced_total > 0 else 0
    
    print(f"Advanced tests: {advanced_passed}/{advanced_total} = {advanced_score:.1f}/40")
    
    total_score = basic_score + intermediate_score + advanced_score
    
    # Generate detailed breakdown
    basic_details = []
    intermediate_details = []
    advanced_details = []
    
    # Add test details if available
    if basic_data and 'tests' in basic_data:
        for test in basic_data['tests']:
            status = '✓' if test.get('outcome') == 'passed' else '✗'
            basic_details.append(f"  {status} {test.get('nodeid', 'Unknown test')}")
    
    if intermediate_data and 'tests' in intermediate_data:
        for test in intermediate_data['tests']:
            status = '✓' if test.get('outcome') == 'passed' else '✗'
            intermediate_details.append(f"  {status} {test.get('nodeid', 'Unknown test')}")
    
    if advanced_data and 'tests' in advanced_data:
        for test in advanced_data['tests']:
            status = '✓' if test.get('outcome') == 'passed' else '✗'
            advanced_details.append(f"  {status} {test.get('nodeid', 'Unknown test')}")
    
    # Generate report
    report = f"""
BINARY SEARCH TREE - AUTO-GRADER REPORT
=====================================

Basic Operations (25 points):      {basic_score:.1f}/25 ({basic_passed}/{basic_total} tests passed)
Traversals & Properties (35 points): {intermediate_score:.1f}/35 ({intermediate_passed}/{intermediate_total} tests passed)
Advanced Features (40 points):     {advanced_score:.1f}/40 ({advanced_passed}/{advanced_total} tests passed)

TOTAL SCORE: {total_score:.1f}/100
Grade: {get_letter_grade(total_score)}

Feature Breakdown:
- Insert/Search: {'✓' if basic_score > 15 else '✗'}
- Traversals: {'✓' if intermediate_score > 20 else '✗'}
- Tree Properties: {'✓' if intermediate_score > 20 else '✗'}
- Deletion: {'✓' if advanced_score > 25 else '✗'}
- BST Validation: {'✓' if advanced_score > 25 else '✗'}

Detailed Test Results:
----------------------
Basic Tests:
{chr(10).join(basic_details) if basic_details else '  No detailed results available'}

Intermediate Tests:
{chr(10).join(intermediate_details) if intermediate_details else '  No detailed results available'}

Advanced Tests:
{chr(10).join(advanced_details) if advanced_details else '  No detailed results available'}
"""
    
    with open('grade_report.txt', 'w') as f:
        f.write(report)
    
    print(report)
    
    # Also print JSON structure for debugging (first run only)
    if basic_data:
        print("\n--- DEBUG: Sample JSON structure ---")
        print("Keys in basic_results.json:", list(basic_data.keys()))
        if 'summary' in basic_data:
            print("Keys in summary:", list(basic_data['summary'].keys()))

def get_letter_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

if __name__ == "__main__":
    calculate_grade()