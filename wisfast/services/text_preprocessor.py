import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

class TextPreprocessor:
    def __init__(self):
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords', quiet=True)
        try:
            nltk.data.find('tokenizers/punkt_tab')
        except LookupError:
            nltk.download('punkt_tab', quiet=True)
            nltk.download('punkt', quiet=True)
            
        self.stop_words = set(stopwords.words('french'))
        self.punctuation = set(string.punctuation)

    def clean(self, text: str) -> str:
        # Lowercase
        text = text.lower()
        # Tokenize
        tokens = word_tokenize(text, language='french')
        # Remove punctuation and stopwords
        cleaned_tokens = [
            token for token in tokens
            if token not in self.punctuation and token not in self.stop_words and not token.isnumeric()
        ]
        return " ".join(cleaned_tokens)