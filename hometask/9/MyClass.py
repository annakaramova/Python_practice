import SoftAssert as soft


# implement class and test with soft assertions
class MyClass(object):
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def multiply(self, value):
        self.value *= value

    def divide(self, value):
        self.value /= value

    def test_divide(self):
        with soft.SoftAssert() as sa:
            self.set_value(10)
            self.divide(2)
            sa.assert_that(self.get_value(), 5)
            self.divide(0)
            sa.assert_that(self.get_value(), 5)
            sa.assert_all()
