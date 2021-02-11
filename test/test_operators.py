from src.main import add, sub, mul

def test_add():
    assert add(1, 4) == 5

def test_sub():
    assert sub(1, 4) == -3

def test_mul():
    assert mul(4, 4) == 16
