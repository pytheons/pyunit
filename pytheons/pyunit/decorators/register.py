def as_test(function):
    def decorated_by(*args, **kwargs):
        function.decorated_by = 'test'
        return function

    return decorated_by


def marked_as_test(class_name, function_name):
    function = getattr(class_name, function_name)
    attribute = getattr(function, 'decorated_by', None)

    return attribute is not None and attribute == 'test'
