"""
fraud_detection.py - PII Detection and Metadata Forensics
"""
import re
import io
from typing import List, Optional
from pypdf import PdfReader

def detect_pii(text: str) -> tuple:
    """Detects PAN and Aadhaar in text. Returns (detected_list, confidence).
    Confidence increases with number of PII types found.
    """
    detected = []
    if not text: return detected, 0.0
    if re.findall(r'\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b', text.upper()):
        detected.append("PAN_DETECTED")
    aadhaar_pattern = r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'
    if re.findall(aadhaar_pattern, text):
        detected.append("AADHAAR_DETECTED")
    
    # Confidence based on number of PII types: 1 type=0.75, 2 types=0.95
    confidence = 0.75 if len(detected) == 1 else (0.95 if len(detected) > 1 else 0.0)
    return detected, confidence

def analyze_metadata(file_bytes: bytes, extracted_text: str) -> tuple:
    """Compares hidden file year with visible text year. Returns (message, confidence) or (None, 0.0).
    Confidence increases with severity of discrepancy.
    """
    try:
        reader = PdfReader(io.BytesIO(file_bytes))
        meta = reader.metadata
        if not meta: return None, 0.0

        creation_date = str(meta.get('/CreationDate', ''))
        year_match = re.search(r'(\d{4})', creation_date)
        if year_match:
            pdf_year = int(year_match.group(1))
            text_years = [int(y) for y in re.findall(r'\b(20\d{2})\b', extracted_text)]
            if text_years and pdf_year > max(text_years):
                year_diff = pdf_year - max(text_years)
                # Higher confidence for larger year gaps (4+ years = 0.92, 1-3 years = 0.78)
                confidence = 0.92 if year_diff >= 4 else 0.78
                return "METADATA_MISMATCH: Hidden year is later than document year", confidence
        
        # Check Creator/Producer for Canva markers in PDF
        creator = str(meta.get('/Creator', '')).lower()
        if 'canva' in creator: 
            return "SUSPICIOUS_CREATOR_TOOL: Canva", 0.85
    except: pass
    return None, 0.0

