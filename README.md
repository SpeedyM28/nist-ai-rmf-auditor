# NIST AI RMF + ISO 42001 Auditor

[![Live Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nist-ai-rmf-auditor.streamlit.app)

An automated AI governance tool that analyzes organizational AI policies against **NIST AI RMF 1.0** and **ISO/IEC 42001:2023** using Gemini LLMs. Identifies compliance gaps and generates detailed audit reports.

---

## Live Demo

Try the tool live: **[https://nist-ai-rmf-auditor.streamlit.app](https://nist-ai-rmf-auditor.streamlit.app)**

Upload your AI policy and get a compliance report instantly.

---

## Why This Tool Exists

Organizations deploying AI need to govern it responsibly. NIST AI RMF and ISO 42001 provide frameworks, but manually auditing policies against these standards is time-consuming and error-prone.

This tool automates the gap analysis:

- **Input**: Any AI policy document (PDF, DOCX, Markdown, TXT)
- **Output**: Structured report showing:
  - ✅ Compliant requirements
  - 🟡 Partially compliant requirements
  - ❌ Gaps with explanations and recommendations

---

## Features

- **Multi-format support**: PDF, DOCX, Markdown, plain text
- **Dual-framework auditing**: NIST AI RMF 1.0 + ISO/IEC 42001:2023
- **Gemini LLM integration**: Powered by Google Gemini (3.1 Flash-Lite to 3.1 Pro)
- **Structured reports**: Markdown, HTML, or JSON output
- **Web Interface**: Upload and analyze policies via Streamlit UI
- **Portfolio-ready**: Designed to demonstrate AI governance expertise

---

## Installation

```
# Clone the repository
git clone https://github.com/SpeedyM28/nist-ai-rmf-auditor.git
cd nist-ai-rmf-auditor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your GOOGLE_API_KEY to .env
```

---

## Usage

### CLI (Command Line Interface)

```
# Basic usage
python src/main.py --policy path/to/policy.pdf --output report.md

# With custom model and format
python src/main.py \
  --policy path/to/policy.pdf \
  --output report.html \
  --model gemini-3.6-flash \
  --format html
```

### Web Interface (Streamlit)

```
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

### Options

| Flag | Description | Default |
| :--- | :--- | :--- |
| `--policy` | Path to AI policy document (PDF, DOCX, MD, TXT) | Required |
| `--output` | Output file path | `report.md` |
| `--model` | Gemini model to use | `gemini-3.6-flash` |
| `--format` | Output format (markdown, html, json) | `markdown` |
| `--knowledge-base` | Path to knowledge base JSON | `src/knowledge_base/knowledge_base.json` |

---

## Test Results

### Mock Policy Test (Simple policy with deliberate gaps)

| Metric | Count |
| :--- | :--- |
| Total Requirements | 37 |
| Compliant | 3 |
| Partial | 11 |
| Gaps | 23 |
| Compliance Rate | **8.1%** |

✅ The tool identified gaps in the intentionally incomplete policy.

### NIST AI RMF 1.0 PDF Test (Full 48-page document, 106,000 characters)

| Metric | Count |
| :--- | :--- |
| Total Requirements | 37 |
| Compliant | 18 |
| Partial | 15 |
| Gaps | 4 |
| Compliance Rate | **48.6%** |

✅ The tool correctly recognized NIST's own document as highly compliant with itself.  
✅ The **4 gaps** are legitimate missing elements in the framework document itself.

**The 4 gaps found:**
- **GOVERN-1.6**: No AI system inventory mechanism
- **GOVERN-2.2**: No training/competency requirements
- **GOVERN-6.2**: No contingency plans for third-party failures
- **MAP-3.4**: No operator proficiency standards

### Microsoft AI Policy Test (Full comprehensive policy)

| Metric | Count |
| :--- | :--- |
| Total Requirements | 37 |
| Compliant | 36 |
| Partial | 0 |
| Gaps | 1 |
| Compliance Rate | **97.3%** |

✅ The tool correctly recognized Microsoft's comprehensive AI governance framework.  
✅ The **1 gap** is a genuine omission—no explicit decommissioning procedures for AI systems.

**The 1 gap found:**
- **GOVERN-1.7**: No decommissioning/retirement procedures for AI systems

---

## Model Selection

| Model | Cost | Use Case |
| :--- | :--- | :--- |
| `gemini-3.1-flash-lite` | 💰 Cheapest | Quick tests, simple policies |
| `gemini-3.5-flash` | 💰💰 Moderate | General use |
| `gemini-3.6-flash` | 💰💰💰 Balanced | **Best balance of cost & quality** (default) |
| `gemini-3.7-flash` | 💰💰💰💰 More capable | Complex, nuanced policies |
| `gemini-3.1-pro` | 💰💰💰💰💰 Most powerful | Deep analysis of large documents |

---

## Configuration

### Character Limit

The tool **does not impose a character limit** by default. The full policy text is sent to the LLM for maximum accuracy.

Gemini models have a **1M token context window**—they can handle full policy documents.

To add a limit (if needed), edit `src/engine/auditor.py` in the `_build_prompt` method:

```
policy_preview = policy_text[:50000]  # Add this line to limit
```

---

## Deployment

The tool is deployed on **Streamlit Community Cloud**:

**[https://nist-ai-rmf-auditor.streamlit.app](https://nist-ai-rmf-auditor.streamlit.app)**

To deploy your own instance:
1. Fork the repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select the repository and branch
5. Set the main file to `app.py`
6. Add your `GOOGLE_API_KEY` in the secrets section
7. Click "Deploy"

---

## Note on API Usage

This tool relies on the Google Gemini API, which operates under usage quotas and rate limits. While the application is designed to handle typical policy documents efficiently, performance may vary based on:

- Document length and complexity
- Concurrent usage and API availability
- Daily quota consumption

The tool is hosted on the Streamlit Community Cloud free tier, which provides a demonstration environment for individual use. For production workloads or enterprise deployment, consider implementing additional error handling, request queuing, and monitoring to ensure reliable operation at scale.

---

## Project Structure

```
nist-ai-rmf-auditor/
├── app.py                     # Streamlit web interface
├── src/
│   ├── main.py                # CLI entry point
│   ├── knowledge_base/
│   │   └── knowledge_base.json # NIST AI RMF + ISO 42001 requirements
│   ├── engine/
│   │   ├── extractor.py       # PDF/DOCX/MD text extraction
│   │   └── auditor.py         # LLM gap analysis logic
│   └── reporting/
│       └── report_generator.py # Markdown/HTML/JSON report generation
├── tests/
│   └── sample_policies/       # Sample policies for testing
├── .env                       # GOOGLE_API_KEY
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.12+
- Google Gemini API key ([Get one here](https://aistudio.google.com/))
- Dependencies listed in `requirements.txt`

---

## Future Improvements

- [x] Streamlit web interface
- [x] Full document processing (no character limit)
- [ ] Additional model support (Claude, OpenAI, open-source)
- [ ] Real-time policy drafting with LLM-powered suggestions
- [ ] Integration with GRC tools (Archer, ServiceNow GRC)
- [ ] Export to PDF, Excel, and other formats
- [ ] Enterprise-grade rate limit handling and monitoring

---

## License

MIT

---

## Contact

Built by **Jamil Bitar**

- [LinkedIn](https://www.linkedin.com/in/jamil-bitar/)
- [GitHub](https://github.com/SpeedyM28/)

---

## Acknowledgments

- [NIST AI RMF 1.0](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC 42001:2023](https://www.iso.org/standard/81230.html) - Artificial Intelligence Management System
- [Google Gemini](https://ai.google.dev/) - LLM API

---

**Last Updated:** August 2026
```