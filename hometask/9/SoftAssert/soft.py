# implement soft assertions


class SoftAssert(object):
    def __init__(self, softly=True):
        self.softly = softly
        self.assertions = []

    def assert_that(self, actual, expected):
        if actual == expected:
            self.assertions.append(True)
        else:
            self.assertions.append(False)
            if not self.softly:
                raise AssertionError("Actual value: %s, Expected value: %s" % (actual, expected))

    def assert_all(self):
        if not all(self.assertions):
            raise AssertionError("One or more assertions failed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.assert_all()
        return False

