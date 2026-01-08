# text_analyzer/tokenizers.py

from nltk.tokenize import sent_tokenize, word_tokenize
import tiktoken


def tokenize_text(text: str):
    """
    Perform sentence, word, and LLM-style tokenization.
    Returns results in a dictionary.
    """

    if not text or not text.strip():
        return {
            "sentences": [],
            "words": [],
            "llm_tokens": [],
            "llm_token_count": 0,
            "estimated_cost": 0.0,
        }

    # Sentence tokenization
    sentences = sent_tokenize(text)

    # Word tokenization
    words = word_tokenize(text)

    # LLM tokenization (GPT-4)
    encoder = tiktoken.encoding_for_model("gpt-4")
    token_ids = encoder.encode(text)
    llm_tokens = [encoder.decode([t]) for t in token_ids]

    # Cost estimation (example rate)
    cost_per_token = 0.00003
    estimated_cost = len(token_ids) * cost_per_token

    return {
        "sentences": sentences,
        "sentence_count": len(sentences),
        "words": words,
        "word_count": len(words),
        "llm_tokens": llm_tokens,
        "llm_token_count": len(token_ids),
        "estimated_cost": round(estimated_cost, 6),
    }


