#!/usr/bin/env python3
"""
Parses SCAN-RESULTS.md to extract baseline vulnerability count (critical + high).

For SAST/OWASP Dependency-Check format.

Usage:
  python3 scripts/parse-baseline.py ../SCAN-RESULTS.md

Returns: integer count of critical + high vulnerabilities
"""

import sys
import re


def parse_java_baseline(file_path):
    """Parse Java SCAN-RESULTS.md and count critical + high vulnerabilities."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Could not find {file_path}", file=sys.stderr)
        sys.exit(1)

    critical_count = 0
    high_count = 0

    # Parse the format:
    # "Found 2 issues of Very High severity."
    # "Found 14 issues of High severity."

    lines = content.split('\n')
    for line in lines:
        line_lower = line.lower()

        # Look for "Found X issues of Very High severity" or "Found X issues of High severity"
        match = re.search(r'found (\d+) issues? of (?:very )?high severity', line_lower, re.IGNORECASE)
        if match:
            count = int(match.group(1))
            if 'very high' in line_lower:
                critical_count += count
            else:
                high_count += count

        # Alternative: count individual vulnerability lines
        # "CWE-78: ... (CRITICAL)" or "(HIGH)"
        if '(critical)' in line_lower:
            critical_count += 1
        elif '(high)' in line_lower:
            high_count += 1

    total = critical_count + high_count
    return total


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/parse-baseline.py <SCAN-RESULTS.md>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    baseline = parse_java_baseline(file_path)
    print(baseline)
