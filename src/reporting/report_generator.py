# src/reporting/report_generator.py

import os
import json
from datetime import datetime
from typing import Dict, Any


class ReportGenerator:
    """Generates audit reports in various formats."""
    
    def __init__(self, knowledge_base_path: str, output_path: str):
        self.knowledge_base_path = knowledge_base_path
        self.output_path = output_path
        
        # Load knowledge base for context
        with open(knowledge_base_path, 'r') as f:
            self.kb = json.load(f)
    
    def _generate_markdown(self, results: Dict[str, Any]) -> str:
        """Generate a markdown report."""
        summary = results.get("summary", {})
        findings = results.get("results", [])
        
        report = f"""# NIST AI RMF + ISO 42001 Audit Report

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Executive Summary

| Metric | Count |
| :--- | :--- |
| Total Requirements | {summary.get("total_requirements", 0)} |
| Compliant | {summary.get("compliant", 0)} |
| Partial | {summary.get("partial", 0)} |
| Gaps | {summary.get("gaps", 0)} |

**Compliance Rate:** {summary.get("compliant", 0) / max(summary.get("total_requirements", 1), 1) * 100:.1f}%

---

## Detailed Findings

"""
        
        # Group findings by framework
        nist_findings = []
        iso_findings = []
        
        for finding in findings:
            # Match framework from ID
            if finding.get("id", "").startswith("GOVERN") or finding.get("id", "").startswith("MAP"):
                nist_findings.append(finding)
            else:
                iso_findings.append(finding)
        
        if nist_findings:
            report += "### NIST AI RMF\n\n"
            for finding in nist_findings:
                status = finding.get("status", "UNKNOWN")
                emoji = "✅" if status == "COMPLIANT" else "🟡" if status == "PARTIAL" else "❌"
                report += f"""
#### {emoji} {finding.get('id')} - {status}

**Explanation:** {finding.get('explanation', 'No explanation provided.')}

**Recommendation:** {finding.get('recommendation', 'No recommendation provided.')}

"""
        
        if iso_findings:
            report += "### ISO 42001\n\n"
            for finding in iso_findings:
                status = finding.get("status", "UNKNOWN")
                emoji = "✅" if status == "COMPLIANT" else "🟡" if status == "PARTIAL" else "❌"
                report += f"""
#### {emoji} {finding.get('id')} - {status}

**Explanation:** {finding.get('explanation', 'No explanation provided.')}

**Recommendation:** {finding.get('recommendation', 'No recommendation provided.')}

"""
        
        return report
    
    def _generate_html(self, results: Dict[str, Any]) -> str:
        """Generate an HTML report."""
        summary = results.get("summary", {})
        findings = results.get("results", [])
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>NIST AI RMF + ISO 42001 Audit Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 1000px; margin: 0 auto; padding: 20px; background: #f5f5f5; }}
        .container {{ background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #1a237e; }}
        h2 {{ color: #283593; border-bottom: 2px solid #e8eaf6; padding-bottom: 10px; }}
        h3 {{ color: #1a237e; margin-top: 30px; }}
        .summary {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 15px; margin: 20px 0; }}
        .stat {{ background: #e8eaf6; padding: 15px; border-radius: 8px; text-align: center; }}
        .stat-number {{ font-size: 28px; font-weight: bold; }}
        .stat-label {{ color: #555; font-size: 14px; }}
        .finding {{ background: #f8f9fa; padding: 15px; margin: 15px 0; border-radius: 8px; border-left: 4px solid #ccc; }}
        .finding.compliant {{ border-left-color: #4caf50; }}
        .finding.partial {{ border-left-color: #ff9800; }}
        .finding.gap {{ border-left-color: #f44336; }}
        .badge {{ display: inline-block; padding: 3px 10px; border-radius: 12px; color: white; font-size: 12px; font-weight: bold; }}
        .badge.compliant {{ background: #4caf50; }}
        .badge.partial {{ background: #ff9800; }}
        .badge.gap {{ background: #f44336; }}
        .compliance-rate {{ font-size: 48px; text-align: center; margin: 20px 0; }}
        .footer {{ margin-top: 30px; text-align: center; color: #888; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 NIST AI RMF + ISO 42001 Audit Report</h1>
        <p><strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        
        <h2>Executive Summary</h2>
        <div class="summary">
            <div class="stat">
                <div class="stat-number">{summary.get('total_requirements', 0)}</div>
                <div class="stat-label">Total Requirements</div>
            </div>
            <div class="stat">
                <div class="stat-number" style="color: #4caf50;">{summary.get('compliant', 0)}</div>
                <div class="stat-label">Compliant</div>
            </div>
            <div class="stat">
                <div class="stat-number" style="color: #ff9800;">{summary.get('partial', 0)}</div>
                <div class="stat-label">Partial</div>
            </div>
            <div class="stat">
                <div class="stat-number" style="color: #f44336;">{summary.get('gaps', 0)}</div>
                <div class="stat-label">Gaps</div>
            </div>
        </div>
        
        <div class="compliance-rate">
            {summary.get('compliant', 0) / max(summary.get('total_requirements', 1), 1) * 100:.1f}% Compliance Rate
        </div>
        
        <h2>Detailed Findings</h2>
        
        <h3>NIST AI RMF</h3>
"""
        
        for finding in findings:
            if finding.get("id", "").startswith("GOVERN") or finding.get("id", "").startswith("MAP"):
                status = finding.get("status", "UNKNOWN").lower()
                emoji = "✅" if status == "compliant" else "🟡" if status == "partial" else "❌"
                html += f"""
        <div class="finding {status}">
            <h4>{emoji} {finding.get('id')} <span class="badge {status}">{finding.get('status', 'UNKNOWN')}</span></h4>
            <p><strong>Explanation:</strong> {finding.get('explanation', 'No explanation provided.')}</p>
            <p><strong>Recommendation:</strong> {finding.get('recommendation', 'No recommendation provided.')}</p>
        </div>
"""
        
        html += """
        <h3>ISO 42001</h3>
"""
        
        for finding in findings:
            if not (finding.get("id", "").startswith("GOVERN") or finding.get("id", "").startswith("MAP")):
                status = finding.get("status", "UNKNOWN").lower()
                emoji = "✅" if status == "compliant" else "🟡" if status == "partial" else "❌"
                html += f"""
        <div class="finding {status}">
            <h4>{emoji} {finding.get('id')} <span class="badge {status}">{finding.get('status', 'UNKNOWN')}</span></h4>
            <p><strong>Explanation:</strong> {finding.get('explanation', 'No explanation provided.')}</p>
            <p><strong>Recommendation:</strong> {finding.get('recommendation', 'No recommendation provided.')}</p>
        </div>
"""
        
        html += f"""
        <div class="footer">
            Generated by NIST AI RMF + ISO 42001 Auditor
        </div>
    </div>
</body>
</html>
"""
        return html
    
    def generate(self, results: Dict[str, Any], format_type: str = "markdown") -> None:
        """Generate and save the report."""
        if format_type == "markdown":
            content = self._generate_markdown(results)
        elif format_type == "html":
            content = self._generate_html(results)
        else:
            content = json.dumps(results, indent=2)
        
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(content)