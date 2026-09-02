# app.py

import streamlit as st
import os
import tempfile
from pathlib import Path

# Import your existing modules
from src.engine.extractor import DocumentExtractor
from src.engine.auditor import AIAuditor
from src.reporting.report_generator import ReportGenerator

# Page configuration
st.set_page_config(
    page_title="NIST AI RMF + ISO 42001 Auditor",
    page_icon="🧠",
    layout="wide"
)

# Title
st.title("🧠 NIST AI RMF + ISO 42001 Auditor")
st.markdown("Automated AI policy gap analysis against NIST AI RMF 1.0 and ISO/IEC 42001:2023")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Model selection
    model_options = [
        "gemini-3.1-flash-lite",
        "gemini-3.5-flash",
        "gemini-3.6-flash",
        "gemini-3.7-flash",
        "gemini-3.1-pro"
    ]
    selected_model = st.selectbox(
        "Select Gemini Model",
        model_options,
        index=2  # Default to 3.6-flash
    )
    
    st.caption("💡 3.6 Flash offers the best balance of cost and quality")
    
    # NEW: NCA-ECC toggle
    nca_mode = st.checkbox(
        "🇸🇦 Export for Saudi NCA-ECC Compliance",
        help="Maps NIST AI RMF findings to Saudi NCA-ECC controls for KSA regulatory alignment"
    )

# Main area - two columns
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📤 Upload Policy Document")
    
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["pdf", "docx", "md", "txt"],
        help="Upload your AI policy document (PDF, DOCX, Markdown, or plain text)"
    )
    
    if uploaded_file is not None:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        st.info(f"📄 Size: {uploaded_file.size / 1024:.1f} KB")

    # Generate button
    generate_button = st.button(
        "🔍 Generate Report",
        type="primary",
        disabled=uploaded_file is None
    )

with col2:
    st.subheader("📊 Report")
    
    # Placeholder for report content
    report_placeholder = st.empty()

# Processing logic
if generate_button and uploaded_file is not None:
    try:
        # Save uploaded file to temp location
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name
        
        # Extract text
        with st.spinner("📄 Extracting text from document..."):
            extractor = DocumentExtractor()
            policy_text = extractor.extract(tmp_path)
        
        # Clean up temp file
        os.unlink(tmp_path)

        # Get API key from environment or Streamlit secrets
        api_key = os.environ.get("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

        if not api_key:
            st.error("❌ GOOGLE_API_KEY not found. Please add it to Streamlit secrets.")
            st.stop()
        
        # Initialize auditor
        kb_path = "src/knowledge_base/knowledge_base.json"
        auditor = AIAuditor(kb_path, selected_model, api_key=api_key)
        
        # Run audit
        with st.spinner(f"🧠 Analyzing policy with {selected_model}..."):
            results = auditor.audit(policy_text)
        
        # Generate report
        with st.spinner("📊 Generating report..."):
            # Save report to temp file
            report_path = tempfile.NamedTemporaryFile(delete=False, suffix=".md").name
            generator = ReportGenerator(kb_path, report_path)
            # NEW: pass nca_mode flag
            generator.generate(results, "markdown", nca_mode=nca_mode)
            
            # Read report content
            with open(report_path, 'r', encoding='utf-8') as f:
                report_content = f.read()
            
            os.unlink(report_path)
        
        # Display summary
        summary = results.get("summary", {})
        total = summary.get("total_requirements", 0)
        compliant = summary.get("compliant", 0)
        partial = summary.get("partial", 0)
        gaps = summary.get("gaps", 0)
        rate = (compliant / max(total, 1)) * 100
        
        with col2:
            # NEW: Show NCA badge
            badge = "🇸🇦 NCA-ECC Mode" if nca_mode else "🧠 Standard Mode"
            report_placeholder.markdown(f"""
            ### ✅ Audit Complete
            **Mode:** {badge}
            
            | Metric | Count |
            | :--- | :--- |
            | Total Requirements | {total} |
            | ✅ Compliant | {compliant} |
            | 🟡 Partial | {partial} |
            | ❌ Gaps | {gaps} |
            | **Compliance Rate** | **{rate:.1f}%** |
            """)
            
            # Download button
            st.download_button(
                label="📥 Download Report (Markdown)",
                data=report_content,
                file_name="audit_report.md",
                mime="text/markdown"
            )
        
        # Display detailed findings in expandable section
        with st.expander("📋 View Detailed Findings", expanded=True):
            st.markdown(report_content)
        
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
        st.stop()

# Footer
st.markdown("---")
st.caption("Built with ❤️ using NIST AI RMF 1.0, ISO/IEC 42001:2023, and Google Gemini")