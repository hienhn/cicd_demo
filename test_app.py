from app import add


def test_add_return_the_sum():
    assert 3 == add(1,2)
    assert 0 == add(0,0)
    assert -1 == add(-2,1)