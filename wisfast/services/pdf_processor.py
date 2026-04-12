import PyPDF2
from dataclasses import dataclass
from typing import List
import logging

logger = logging.getLogger(__name__)

@dataclass
class PageText:
    page_number: int
    raw_text: str

class PDFProcessor:
    @staticmethod
    def extract_pages(pdf_path: str, callback=None) -> List[PageText]:
        pages = []
        try:
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                for i, page in enumerate(reader.pages):
                    # Check if processing should stop
                    if callback and callback(i + 1, len(reader.pages)):
                        logger.info("Extraction interrupted by callback.")
                        return []
                        
                    text = page.extract_text()
                    if text and text.strip():
                        pages.append(PageText(page_number=i + 1, raw_text=text.strip()))
                    else:
                        logger.warning(f"Empty or unreadable text on page {i + 1} of {pdf_path}")
        except Exception as e:
            logger.error(f"Failed to process PDF {pdf_path}: {e}")
            raise
        return pages
