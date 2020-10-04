from pytheons.pyunit.decorators import register


def test(function):
    @register.as_test(function)
    def test_method(*args, **kwargs):
        function(*args, **kwargs)

    return test_method
