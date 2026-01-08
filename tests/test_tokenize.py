from text_analyzer.tokenizers import tokenize_text


def test_tokenize_returns_dict():
    result = tokenize_text("Hello world")
    assert isinstance(result, dict)


def test_sentence_count():
    result = tokenize_text("Hello world. How are you?")
    assert result["sentence_count"] == 2


def test_word_tokens_present():
    result = tokenize_text("Hello world")
    assert "Hello" in result["words"]
    assert "world" in result["words"]


def test_llm_token_count():
    result = tokenize_text("Tokenization")
    assert result["llm_token_count"] > 0
