# src/engine/auditor.py

import json
import os
from typing import List, Dict, Any, Optional
from pathlib import Path

try:
    import google.generativeai as genai
except ImportError:
    genai = None

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class AIAuditor:
    """Uses LLM to analyze AI policies against NIST AI RMF and ISO 42001."""
    
    def __init__(self, knowledge_base_path: str, model_name: str = "gemini-1.5-flash", api_key: str = None):
        """Initialize the auditor with a knowledge base."""
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
        self.model_name = model_name
        
        # Initialize Gemini if available
        if genai is not None:
            key_to_use = api_key or os.environ.get("GOOGLE_API_KEY")
            if key_to_use:
                genai.configure(api_key=key_to_use)
                self.model = genai.GenerativeModel(model_name)
            else:
                print("Warning: GOOGLE_API_KEY not set. Set it with: export GOOGLE_API_KEY='your-key'")
                self.model = None
        else:
            print("Warning: google-generativeai not installed. Run: pip install google-generativeai")
            self.model = None
    
    def _load_knowledge_base(self, path: str) -> Dict[str, Any]:
        """Load the knowledge base from a JSON file."""
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _build_prompt(self, policy_text: str) -> str:
        """Build the prompt for the LLM."""
        # Extract requirements from the knowledge base
        requirements = []
        frameworks = self.knowledge_base.get("frameworks", {})
        
        for framework_name, framework in frameworks.items():
            functions = framework.get("functions", {})
            for function_name, function in functions.items():
                categories = function.get("categories", [])
                for category in categories:
                    subcategories = category.get("subcategories", [])
                    for sub in subcategories:
                        requirements.append({
                            "id": sub["id"],
                            "framework": framework_name,
                            "function": function_name,
                            "description": sub["description"],
                            "keywords": sub.get("keywords", [])
                        })
        
        # Build the prompt
        prompt = f"""
            You are an expert AI auditor. Analyze the following AI policy document against NIST AI RMF and ISO/IEC 42001 requirements.

            POLICY DOCUMENT:
            ""{policy_text}""
            REQUIREMENTS TO CHECK:
            ""{json.dumps(requirements, indent=2)}""

            For each requirement, determine if the policy:
            - COMPLIANT: The policy explicitly addresses this requirement
            - PARTIAL: The policy partially addresses it but is missing key elements
            - GAP: The policy does not address this requirement

            Also provide:
            1. A brief explanation for your assessment
            2. Specific recommendations to close any gaps

            OUTPUT FORMAT (JSON only - no other text):
            {{
            "results": [
                {{
                "id": "GOVERN-1.1",
                "status": "COMPLIANT | PARTIAL | GAP",
                "explanation": "Brief explanation here",
                "recommendation": "Specific recommendation here"
                }}
            ],
            "summary": {{
                "total_requirements": 0,
                "compliant": 0,
                "partial": 0,
                "gaps": 0
            }}
            }}
            """
        return prompt
    
    def _parse_response(self, response_text: str) -> Dict[str, Any]:
        """Parse the LLM response into a structured format."""
        try:
            # Extract JSON from the response
            # Some models wrap JSON in markdown code blocks
            if "```json" in response_text:
                start = response_text.find("```json") + 7
                end = response_text.rfind("```")
                response_text = response_text[start:end].strip()
            elif "```" in response_text:
                start = response_text.find("```") + 3
                end = response_text.rfind("```")
                response_text = response_text[start:end].strip()
            
            return json.loads(response_text)
        except json.JSONDecodeError as e:
            print(f"Failed to parse LLM response: {e}")
            print(f"Response was: {response_text[:500]}...")
            return {
                "results": [],
                "summary": {
                    "total_requirements": 0,
                    "compliant": 0,
                    "partial": 0,
                    "gaps": 0
                },
                "raw_response": response_text
            }
    
    def audit(self, policy_text: str) -> Dict[str, Any]:
        """
        Perform a gap analysis on the policy text.
        
        Returns a structured report with compliance findings.
        """
        if self.model is None:
            return {
                "error": "No LLM available. Please set up Google Gemini API key.",
                "results": [],
                "summary": {
                    "total_requirements": 0,
                    "compliant": 0,
                    "partial": 0,
                    "gaps": 0
                }
            }
        
        prompt = self._build_prompt(policy_text)
        
        try:
            response = self.model.generate_content(prompt)
            return self._parse_response(response.text)
        except Exception as e:
            print(f"Error during LLM call: {e}")
            return {
                "error": str(e),
                "results": [],
                "summary": {
                    "total_requirements": 0,
                    "compliant": 0,
                    "partial": 0,
                    "gaps": 0
                }
            }