import pytest

def add(a,b):
    return a+b

# List of tuples
@pytest.mark.parametrize("a,b,Expected",[
                         (3,4,7),
                         (3,2,5),
                         (0,3,3),
                         (0,0,0)],ids=["3+4","3+2","0+3","0+0"])
def test_add(a,b,Expected):
    assert add(a,b) == Expected


# Multiple , will check all four combinations
@pytest.mark.parametrize("a",[1,3])
@pytest.mark.parametrize("b",[10,11])
def test_cross(a,b):
    assert a < b

# Invalid or expected negative case
@pytest.mark.xfail
@pytest.mark.parametrize("a,b,expected",[(1,3,8)])
def test_add_neg(a,b,expected):
    assert add(a,b) == expected