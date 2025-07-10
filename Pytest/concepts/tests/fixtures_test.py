import pytest

# runs once every test function
@pytest.fixture(scope="function")
def sample_data():
    return {"username":"abhishek","password":"demo"}

def test_login_user(sample_data):
    assert sample_data['username'] == "abhishek"

# Teardown with yield
@pytest.fixture(scope="function")
def setup_teardown():
    print("Before running test")
    yield
    print("After running the test")

def test_setup_teardown(setup_teardown):
    print("Test is running currently....")

# can turn autouse to use before every function automatically
@pytest.fixture(autouse=True)
def auto():
    print("fixture ran successfully")
    return {"a":"b"}

def test_au():
    assert 1==1


@pytest.fixture
def setup_data_fix():
    print("Setup Data Start")
    yield {"a":5}
    print("\nSetup Data Clear")

def test_data_fix(setup_data_fix):
    assert setup_data_fix['a'] == 5