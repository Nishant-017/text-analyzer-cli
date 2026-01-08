from text_analyzer.taggers import pos_tagging, ner_bio_tagging


def test_pos_structure():
    result = pos_tagging("Naruto trained hard")
    assert isinstance(result, list)
    assert "token" in result[0]
    assert "pos" in result[0]


def test_ner_entities_present():
    entities, _ = ner_bio_tagging("Elon Musk founded SpaceX")
    assert any(label == "PERSON" for _, label in entities)


def test_bio_tags_exist():
    _, bio = ner_bio_tagging("Elon Musk")
    assert len(bio) > 0
    assert bio[0][1] in ["O", "B-PERSON", "I-PERSON"]
