
class ValidationTime:
    @staticmethod
    def validate_non_negative_int(func):
        def inner(time, val):
            try:
                val = int(val)
                if val < 0:
                    raise ValueError("value cannot be negative")
            except ValueError:
                raise ValueError("value must be a non negative integer")
            return func(time, val)
        return inner


    @staticmethod
    def validate_val_in_range(a,b):
        def inner(func):
            def wrapper(time, val):
                if val < a or val > b:
                    raise ValueError("value is not in range [{},{}]".format(a, b))
                return func(time, val)
            return wrapper
        return inner