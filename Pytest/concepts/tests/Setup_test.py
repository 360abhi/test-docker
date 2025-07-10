class TestMath:

    def setup_method(self):
        print("Setting up before Test \n")

    def teardown_method(self):
        print("Cleaning after test \n")

    def test_add(self):
        assert 5+6 == 11

    def test_multiply(self):
        assert 7-3 == 4

