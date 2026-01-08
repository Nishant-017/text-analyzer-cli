from text_analyzer.normalizers import stem_text, lem_text


def test_stem_structure():
    result = stem_text("running studies")
    assert isinstance(result, list)
    assert "porter" in result[0]
    assert "snowball" in result[0]
    assert "lancaster" in result[0]


def test_stemming_changes_word():
    result = stem_text("running")
    assert result[0]["porter"] == "run"


def test_lemmatization_structure():
    result = lem_text("The Avengers")
    assert isinstance(result, list)
    assert "original" in result[0]
    assert "lemma" in result[0]
    assert "pos" in result[0]


def test_lemmatization_changes_word():
    result = lem_text("fighting")
    assert result[0]["lemma"] == "fight"
