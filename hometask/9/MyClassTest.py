
import SoftAssert as soft
import MyClass


def test_increment():
    with soft.SoftAssert() as sa:
        my_class = MyClass.MyClass()
        my_class.increment()
        sa.assert_that(my_class.get_value(), 1)
        my_class.decrement()
        sa.assert_that(my_class.get_value(), 0)
        sa.assert_all()


def test_decrement():
    with soft.SoftAssert() as sa:
        my_class = MyClass.MyClass(10)
        my_class.decrement()
        sa.assert_that(my_class.get_value(), 9)
        my_class.decrement()
        sa.assert_that(my_class.get_value(), 8)
        sa.assert_all()


def test_multiply():
    with soft.SoftAssert() as sa:
        my_class = MyClass.MyClass(10)
        my_class.multiply(2)
        sa.assert_that(my_class.get_value(), 20)
        my_class.multiply(0)
        sa.assert_that(my_class.get_value(), 20)
        sa.assert_all()


def test_set_value():
    with soft.SoftAssert() as sa:
        my_class = MyClass.MyClass(10)
        my_class.set_value(20)
        sa.assert_that(my_class.get_value(), 20)
        my_class.set_value(0)
        sa.assert_that(my_class.get_value(), 0)
        sa.assert_all()


def test_get_value():
    with soft.SoftAssert() as sa:
        my_class = MyClass.MyClass(10)
        sa.assert_that(my_class.get_value(), 10)
        sa.assert_all()


def test_divide():
    with soft.SoftAssert() as sa:
        my_class = MyClass.MyClass(10)
        my_class.divide(2)
        sa.assert_that(my_class.get_value(), 5)
        my_class.divide(0)
        sa.assert_that(my_class.get_value(), 5)
        sa.assert_all()


if __name__ == '__main__':
    test_increment()
    test_decrement()
    test_multiply()
    test_divide()
    test_set_value()
    test_get_value()
    print("All tests passed")
