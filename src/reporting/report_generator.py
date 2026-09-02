import os
import json
from datetime import datetime
from typing import Dict, Any, List, Optional

class ReportGenerator:
    """Generates audit reports in various formats."""
    
    def __init__(self, knowledge_base_path: str, output_path: str):
        self.knowledge_base_path = knowledge_base_path
        self.output_path = output_path
        
        # Load knowledge base for context
        with open(knowledge_base_path, 'r') as f:
            self.kb = json.load(f)
        
        # Load NCA-ECC crosswalk if it exists
        crosswalk_path = os.path.join(
            os.path.dirname(knowledge_base_path), 
            "nca_ecc_crosswalk.json"
        )
        self.nca_mapping = {}
        if os.path.exists(crosswalk_path):
            with open(crosswalk_path, 'r') as f:
                self.nca_mapping = json.load(f)
    
    def _apply_nca_mapping(self, findings: List[Dict]) -> List[Dict]:
        """Translate NIST IDs to NCA-ECC controls."""
        mapped = []
        for finding in findings:
            finding_copy = finding.copy()
            original_id = finding.get("id", "")
            if original_id in self.nca_mapping:
                finding_copy["id"] = self.nca_mapping[original_id]
                finding_copy["original_nist_id"] = original_id  # preserve for reference
            mapped.append(finding_copy)
        return mapped
    
    def _generate_markdown(self, results: Dict[str, Any], nca_mode: bool = False) -> str:
        """Generate a markdown report."""
        summary = results.get("summary", {})
        findings = results.get("results", [])
        
        # Apply NCA mapping if requested
        if nca_mode and self.nca_mapping:
            findings = self._apply_nca_mapping(findings)
            title = "# NCA-ECC AI Control Gap Analysis (Mapped from NIST AI RMF)"
            note = "**Note:** This report maps NIST AI RMF 1.0 requirements to Saudi NCA-ECC controls. The LLM audited against NIST AI RMF; the control IDs have been translated to their NCA-ECC equivalents for KSA regulatory alignment."
        else:
            title = "# NIST AI RMF + ISO 42001 Audit Report"
            note = ""
        
        report = f"""{title}

**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

{note}

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
        
        # Group findings by framework (using original NIST IDs if available)
        nist_findings = []
        iso_findings = []
        
        for finding in findings:
            # If we're in NCA mode, we translated the IDs. 
            # But we can check original_nist_id to know it's NIST.
            if nca_mode and self.nca_mapping:
                # In NCA mode, all mapped IDs are NIST-derived.
                # But ISO findings will remain unmapped (or we can check if they have 'ISO' in ID).
                if "original_nist_id" in finding:
                    nist_findings.append(finding)
                else:
                    iso_findings.append(finding)
            else:
                # Normal mode
                if finding.get("id", "").startswith("GOVERN") or finding.get("id", "").startswith("MAP") or finding.get("original_nist_id"):
                    nist_findings.append(finding)
                else:
                    iso_findings.append(finding)
        
        if nca_mode:
            report += "### NCA-ECC Controls (Derived from NIST AI RMF)\n\n"
        else:
            report += "### NIST AI RMF\n\n"
        
        for finding in nist_findings:
            status = finding.get("status", "UNKNOWN")
            emoji = "✅" if status == "COMPLIANT" else "🟡" if status == "PARTIAL" else "❌"
            # Show original NIST ID if we're in NCA mode
            display_id = finding.get("id")
            if nca_mode and self.nca_mapping and "original_nist_id" in finding:
                display_id = f"{finding.get('id')} (mapped from {finding.get('original_nist_id')})"
            report += f"""
#### {emoji} {display_id} - {status}

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
    
    def _generate_html(self, results: Dict[str, Any], nca_mode: bool = False) -> str:
        """Generate an HTML report."""
        summary = results.get("summary", {})
        findings = results.get("results", [])
        
        if nca_mode and self.nca_mapping:
            findings = self._apply_nca_mapping(findings)
            title = "NCA-ECC AI Control Gap Analysis"
            subtitle = "Mapped from NIST AI RMF 1.0 to Saudi NCA-ECC controls"
        else:
            title = "NIST AI RMF + ISO 42001 Audit Report"
            subtitle = ""
        
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
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
        .mapping-note {{ background: #e3f2fd; padding: 15px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #1a237e; }}
        .footer {{ margin-top: 30px; text-align: center; color: #888; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 {title}</h1>
        {f'<p><strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>' if not nca_mode else ''}
        {f'<p><strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>' if nca_mode else ''}
        {f'<div class="mapping-note"><strong>📌 Saudi NCA-ECC Mapping:</strong> This report maps NIST AI RMF 1.0 requirements to Saudi NCA-ECC controls. The LLM audited against NIST AI RMF; the control IDs have been translated for KSA regulatory alignment.</div>' if nca_mode else ''}
        
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
        
        <h3>{'NCA-ECC Controls (mapped from NIST AI RMF)' if nca_mode else 'NIST AI RMF'}</h3>
"""
        
        # Filter findings for NIST/NCA
        nist_findings = []
        iso_findings = []
        for finding in findings:
            if nca_mode and self.nca_mapping:
                if "original_nist_id" in finding:
                    nist_findings.append(finding)
                else:
                    iso_findings.append(finding)
            else:
                if finding.get("id", "").startswith("GOVERN") or finding.get("id", "").startswith("MAP") or finding.get("original_nist_id"):
                    nist_findings.append(finding)
                else:
                    iso_findings.append(finding)
        
        for finding in nist_findings:
            status = finding.get("status", "UNKNOWN").lower()
            emoji = "✅" if status == "compliant" else "🟡" if status == "partial" else "❌"
            display_id = finding.get("id")
            if nca_mode and self.nca_mapping and "original_nist_id" in finding:
                display_id = f"{finding.get('id')} (mapped from {finding.get('original_nist_id')})"
            html += f"""
        <div class="finding {status}">
            <h4>{emoji} {display_id} <span class="badge {status}">{finding.get('status', 'UNKNOWN')}</span></h4>
            <p><strong>Explanation:</strong> {finding.get('explanation', 'No explanation provided.')}</p>
            <p><strong>Recommendation:</strong> {finding.get('recommendation', 'No recommendation provided.')}</p>
        </div>
"""
        
        if iso_findings:
            html += """
        <h3>ISO 42001</h3>
"""
            for finding in iso_findings:
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
    
    def generate(self, results: Dict[str, Any], format_type: str = "markdown", nca_mode: bool = False) -> None:
        """Generate and save the report."""
        if format_type == "markdown":
            content = self._generate_markdown(results, nca_mode)
        elif format_type == "html":
            content = self._generate_html(results, nca_mode)
        else:
            content = json.dumps(results, indent=2)
        
        with open(self.output_path, 'w', encoding='utf-8') as f:
            f.write(content)