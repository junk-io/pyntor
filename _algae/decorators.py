import functools

def return_on_exception(exception, return_value):
    def decorator(method):
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            try:
                return method(*args, **kwargs)
            except exception:
                return return_value
        return wrapper
    return decorator

def raise_instead(old_exception, new_exception):
    def decorator(method):
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            try:
                return method(*args, **kwargs)
            except old_exception as exc:
                raise new_exception(str(exc))
        return wrapper
    return decorator
