# NIST AI RMF + ISO 42001 Auditor

An automated AI governance tool that analyzes organizational AI policies against **NIST AI RMF 1.0** and **ISO/IEC 42001:2023** using Gemini LLMs. Identifies compliance gaps and generates detailed audit reports.

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

### Basic Command

```
python src/main.py --policy path/to/policy.pdf --output report.md
```

### Advanced Options

```
python src/main.py \
  --policy path/to/policy.pdf \
  --output report.html \
  --model gemini-3.6-flash \
  --format html
```

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

The tool truncates policy text to **50,000 characters** by default. To modify:

Edit `src/engine/auditor.py` in the `_build_prompt` method:

```
policy_preview = policy_text[:50000]  # Change this value
```

Gemini 1.5 models have a **1M token context window**—you can safely increase the limit.

---

## Project Structure

```
nist-ai-rmf-auditor/
├── src/
│   ├── main.py                 # CLI entry point
│   ├── knowledge_base/
│   │   └── knowledge_base.json # NIST AI RMF + ISO 42001 requirements
│   ├── engine/
│   │   ├── extractor.py        # PDF/DOCX/MD text extraction
│   │   └── auditor.py          # LLM gap analysis logic
│   └── reporting/
│       └── report_generator.py # Markdown/HTML/JSON report generation
├── tests/
│   └── sample_policies/        # Sample policies for testing
├── .env                        # GOOGLE_API_KEY
├── requirements.txt
└── README.md
```

---

## Requirements

- Python 3.12+
- Google Gemini API key ([Get one here](https://aistudio.google.com/))
- Dependencies listed in `requirements.txt`

---

## Next Steps

- [ ] Streamlit web interface (upload + view reports)
- [ ] Additional model support (Claude, OpenAI, open-source)
- [ ] Real-time policy drafting with LLM-powered suggestions
- [ ] Integration with GRC tools (Archer, ServiceNow GRC)

---

## License

MIT

---

## Contact

Built by Jamil Bitar
[[LinkedIn URL](https://www.linkedin.com/in/jamil-bitar/)]  
[[GitHub URL](https://github.com/SpeedyM28/)]

---

## Acknowledgments

- NIST AI RMF 1.0: https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001:2023: Artificial Intelligence Management System

---

**Last Updated:** August 2026