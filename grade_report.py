import json
import os

def calculate_grade():
    total_score = 0
    max_score = 100
    
    # Basic tests (25 points)
    basic_score = 0
    if os.path.exists('basic_results.json'):
        with open('basic_results.json', 'r') as f:
            basic_results = json.load(f)
            basic_passed = basic_results['summary']['passed']
            basic_total = basic_results['summary']['total']
            basic_score = (basic_passed / basic_total) * 25 if basic_total > 0 else 0
    
    # Intermediate tests (35 points)
    intermediate_score = 0
    if os.path.exists('intermediate_results.json'):
        with open('intermediate_results.json', 'r') as f:
            intermediate_results = json.load(f)
            intermediate_passed = intermediate_results['summary']['passed']
            intermediate_total = intermediate_results['summary']['total']
            intermediate_score = (intermediate_passed / intermediate_total) * 35 if intermediate_total > 0 else 0
    
    # Advanced tests (40 points)
    advanced_score = 0
    if os.path.exists('advanced_results.json'):
        with open('advanced_results.json', 'r') as f:
            advanced_results = json.load(f)
            advanced_passed = advanced_results['summary']['passed']
            advanced_total = advanced_results['summary']['total']
            advanced_score = (advanced_passed / advanced_total) * 40 if advanced_total > 0 else 0
    
    total_score = basic_score + intermediate_score + advanced_score
    
    # Generate report
    report = f"""
BINARY SEARCH TREE - AUTO-GRADER REPORT
=====================================

Basic Operations (25 points):     {basic_score:.1f}/25
Traversals & Properties (35 points): {intermediate_score:.1f}/35  
Advanced Features (40 points):     {advanced_score:.1f}/40

TOTAL SCORE: {total_score:.1f}/100

Grade: {get_letter_grade(total_score)}

Breakdown:
- Insert/Search: {'✓' if basic_score > 20 else '✗'}
- Traversals: {'✓' if intermediate_score > 25 else '✗'}
- Tree Properties: {'✓' if intermediate_score > 25 else '✗'}
- Deletion: {'✓' if advanced_score > 30 else '✗'}
- BST Validation: {'✓' if advanced_score > 30 else '✗'}
"""
    
    with open('grade_report.txt', 'w') as f:
        f.write(report)
    
    print(report)

def get_letter_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else: return 'F'

if __name__ == "__main__":
    calculate_grade()