#!/usr/bin/env python3
"""
Validates OWASP Dependency-Check JSON report for Critical/High vulnerabilities.

Usage:
  python3 scripts/validate-dependency-check.py <report.json>

Exit codes:
  0 - No critical/high vulnerabilities found
  1 - Critical/high vulnerabilities found
"""

import json
import sys


def validate_dependency_check(report_path):
    """Parse dependency-check JSON report and check for critical/high vulnerabilities."""
    try:
        with open(report_path, 'r') as f:
            report = json.load(f)
    except FileNotFoundError:
        print(f"❌ Could not find report at {report_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Could not parse {report_path} as JSON")
        sys.exit(1)

    # Extract vulnerability data
    dependencies = report.get('reportSchema', {}).get('dependencies', [])

    critical_count = 0
    high_count = 0

    print("\n🔍 OWASP Dependency-Check Vulnerability Summary:\n")

    for dep in dependencies:
        vulns = dep.get('vulnerabilities', [])
        if not vulns:
            continue

        dep_name = dep.get('name', 'unknown')
        for vuln in vulns:
            severity = vuln.get('severity', 'unknown')
            cve = vuln.get('name', '')

            if severity == 'CRITICAL':
                critical_count += 1
                print(f"  🔴 {dep_name}: {cve} ({severity})")
            elif severity == 'HIGH':
                high_count += 1
                print(f"  🟠 {dep_name}: {cve} ({severity})")

    total_critical_high = critical_count + high_count

    print(f"\n📊 Totals:")
    print(f"  Critical: {critical_count}")
    print(f"  High:     {high_count}")
    print(f"  Total:    {total_critical_high}")

    if total_critical_high > 0:
        print(f"\n❌ Found {total_critical_high} critical/high vulnerabilities that need fixing.")
        print("Check SCAN-RESULTS.md for guidance on fixing these issues.")
        return False
    else:
        print(f"\n✅ No critical or high vulnerabilities detected!")
        return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/validate-dependency-check.py <report.json>")
        sys.exit(1)

    report_path = sys.argv[1]
    success = validate_dependency_check(report_path)
    sys.exit(0 if success else 1)
