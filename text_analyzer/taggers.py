# text_analyzer/taggers.py

from nltk import pos_tag
from nltk.tokenize import word_tokenize
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")


# --------------------------------------------------
# POS TAGGING (NLTK)
# --------------------------------------------------

def pos_tagging(text: str):
    """
    Perform Part-of-Speech tagging using NLTK.
    Returns a list of dictionaries:
    { "token": <word>, "pos": <tag> }
    """

    if not text or not text.strip():
        return []

    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    return [
        {"token": word, "pos": tag}
        for word, tag in tagged
    ]


# --------------------------------------------------
# NER + BIO TAGGING (spaCy)
# --------------------------------------------------

def ner_bio_tagging(text: str):
    """
    Perform Named Entity Recognition and BIO tagging.
    Returns:
      - entities: list of (entity_text, label)
      - bio_tags: list of (token, BIO-tag)
    """

    if not text or not text.strip():
        return [], []

    doc = nlp(text)

    # Extract named entities
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))

    # Generate BIO tags
    bio_tags = []
    for token in doc:
        if token.ent_iob_ == "O":
            bio_tags.append((token.text, "O"))
        else:
            bio_tags.append(
                (token.text, f"{token.ent_iob_}-{token.ent_type_}")
            )

    return entities, bio_tags


# --------------------------------------------------
# Standalone test
# --------------------------------------------------

if __name__ == "__main__":
    sample_text = "Elon Musk founded SpaceX in California"

    print("POS TAGGING:")
    for row in pos_tagging(sample_text):
        print(row)

    print("\nNER + BIO TAGGING:")
    entities, bio = ner_bio_tagging(sample_text)
    print("Entities:", entities)
    print("BIO Tags:", bio)
