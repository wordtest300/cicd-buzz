from buzz.generator import generate_buzz


def test_generate_buzz_returns_string():
    result = generate_buzz()
    assert isinstance(result, str)


def test_generate_buzz_not_empty():
    result = generate_buzz()
    assert len(result) > 0
