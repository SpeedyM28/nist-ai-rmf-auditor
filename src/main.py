# src/main.py

import os
import sys
import argparse
import json
from pathlib import Path
from dotenv import load_dotenv

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.engine.extractor import DocumentExtractor
from src.engine.auditor import AIAuditor
from src.reporting.report_generator import ReportGenerator

# Load environment variables from .env file
load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        description="NIST AI RMF + ISO 42001 Auditor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python main.py --policy policy.pdf --output report.md
    python main.py --policy policy.docx --knowledge-base custom_kb.json
        """
    )
    
    parser.add_argument(
        "--policy",
        required=True,
        help="Path to the AI policy document (PDF, DOCX, TXT, MD)"
    )
    
    parser.add_argument(
        "--output",
        default="audit_report.md",
        help="Output file path for the report (default: audit_report.md)"
    )
    
    parser.add_argument(
        "--knowledge-base",
        default="src/knowledge_base/knowledge_base.json",
        help="Path to the knowledge base JSON file"
    )
    
    parser.add_argument(
        "--model",
        default="gemini-3.1-flash-lite",
        help="Gemini model to use (default: gemini-3.1-flash-lite)"
    )
    
    parser.add_argument(
        "--format",
        choices=["markdown", "html", "json"],
        default="markdown",
        help="Output format (default: markdown)"
    )
    
    args = parser.parse_args()
    
    # Check if file exists
    if not os.path.exists(args.policy):
        print(f"Error: Policy file not found: {args.policy}")
        sys.exit(1)
    
    # Check API key
    if not os.environ.get("GOOGLE_API_KEY"):
        print("Warning: GOOGLE_API_KEY not set.")
        print("Set it with: export GOOGLE_API_KEY='your-key'")
        print("Continuing with mock mode...")
    
    print(f"📄 Extracting text from: {args.policy}")
    extractor = DocumentExtractor()
    
    try:
        policy_text = extractor.extract(args.policy)
    except Exception as e:
        print(f"Error extracting document: {e}")
        sys.exit(1)
    
    print(f"📝 Extracted {len(policy_text)} characters")
    
    print(f"🧠 Initializing auditor with knowledge base: {args.knowledge_base}")
    auditor = AIAuditor(args.knowledge_base, args.model)
    
    print("🔍 Analyzing policy...")
    results = auditor.audit(policy_text)
    
    if "error" in results:
        print(f"❌ Audit error: {results['error']}")
        print("Results may be incomplete.")
    
    print(f"📊 Generating report: {args.output}")
    generator = ReportGenerator(args.knowledge_base, args.output)
    generator.generate(results, args.format)
    
    print(f"✅ Report saved to: {args.output}")


if __name__ == "__main__":
    main()