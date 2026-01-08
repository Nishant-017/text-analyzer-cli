# text_analyzer/normalizers.py

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")


# -------------------
# STEMMING
# -------------------

def stem_text(text: str):
    """
    Apply Porter, Snowball, and Lancaster stemming.
    Returns a list of dictionaries.
    """

    if not text or not text.strip():
        return []

    words = word_tokenize(text)

    porter = PorterStemmer()
    snowball = SnowballStemmer("english")
    lancaster = LancasterStemmer()

    results = []

    for word in words:
        results.append({
            "original": word,
            "porter": porter.stem(word),
            "snowball": snowball.stem(word),
            "lancaster": lancaster.stem(word),
        })

    return results


# -------------------
# LEMMATIZATION
# -------------------

def lem_text(text: str):
    """
    Apply spaCy lemmatization with POS tags.
    Returns a list of dictionaries.
    """

    if not text or not text.strip():
        return []

    doc = nlp(text)
    results = []

    for token in doc:
        results.append({
            "original": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
        })

    return results

