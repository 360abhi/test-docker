def subtract(a,b):
    return a-b

def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(5,3) == 2

def test_multiply():
    assert multiply(4,5) == 20

def test_add_negative():
    assert add(3,4) != 5