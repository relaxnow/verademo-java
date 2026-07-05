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
    """Parse Java SCAN-RESULTS.md and count vulnerabilities with CVSS >= 7.0."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Could not find {file_path}", file=sys.stderr)
        sys.exit(1)

    # First, try to extract from the header: "Total Vulnerabilities (CVSS >= 7.0): 150"
    header_pattern = re.compile(r'Total Vulnerabilities \(CVSS >= 7\.0\):\s*(\d+)')
    match = header_pattern.search(content)
    if match:
        return int(match.group(1))

    # Fallback: Parse dependency-check format with CVSS scores:
    # CVE-2015-6420(9.8), CVE-2016-1000031(9.8), CVE-2025-48976(7.5)
    # Count CVEs with CVSS >= 7.0
    count = 0
    cve_pattern = re.compile(r'CVE-\d+-\d+\((\d+\.?\d*)\)')

    for match in cve_pattern.finditer(content):
        cvss = float(match.group(1))
        if cvss >= 7.0:
            count += 1

    return count


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/parse-baseline.py <SCAN-RESULTS.md>", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    baseline = parse_java_baseline(file_path)
    print(baseline)
