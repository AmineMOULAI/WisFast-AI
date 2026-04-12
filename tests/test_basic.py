import pytest
from wisfast.services.text_preprocessor import TextPreprocessor

def test_text_preprocessor():
    preprocessor = TextPreprocessor()
    text = "Ceci est un test de l'application wisFast."
    cleaned = preprocessor.clean(text)
    assert "test" in cleaned.split()
    assert "wisfast" in cleaned.split()
    assert "est" not in cleaned.split()  # Should be removed as stopword
