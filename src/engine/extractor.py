# src/engine/extractor.py

import os
import re
from typing import Optional

try:
    import PyPDF2
except ImportError:
    PyPDF2 = None

try:
    import docx
except ImportError:
    docx = None


class DocumentExtractor:
    """Extracts text from various document formats."""
    
    def __init__(self):
        self.supported_formats = {
            '.pdf': self._extract_pdf,
            '.docx': self._extract_docx,
            '.txt': self._extract_txt,
            '.md': self._extract_txt,
        }
    
    def extract(self, file_path: str) -> Optional[str]:
        """Extract text from a file based on its extension."""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()
        
        if ext not in self.supported_formats:
            raise ValueError(f"Unsupported file format: {ext}")
        
        return self.supported_formats[ext](file_path)
    
    def _extract_pdf(self, file_path: str) -> str:
        """Extract text from PDF using PyPDF2."""
        if PyPDF2 is None:
            raise ImportError("PyPDF2 is not installed. Run: pip install PyPDF2")
        
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = []
            for page in reader.pages:
                page_text = page.extract_text() or ""
                text.append(page_text)
        
        return "\n".join(text)
    
    def _extract_docx(self, file_path: str) -> str:
        """Extract text from Word document."""
        if docx is None:
            raise ImportError("python-docx is not installed. Run: pip install python-docx")
        
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    
    def _extract_txt(self, file_path: str) -> str:
        """Extract text from plain text file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()