from datetime import datetime
import re

class Validation:
    @staticmethod
    def validate_int(val):
        try:
            n = int(val)
        except ValueError:
            raise ValueError("number must be an integer")
        return n
    @staticmethod
    def validate_non_negative_int(val):
        try:
            n = int(val)
            if n<0:
                raise ValueError("number cannot be negative")
        except ValueError:
            raise ValueError("number must be a non negative integer")
        return n

    @staticmethod
    def validate_positive_int(val):
        try:
            n = int(val)
            if n <= 0:
                raise ValueError("number must be positive")
        except ValueError:
            raise ValueError("number must be a positive integer")
        return n

    @staticmethod
    def validate_file_name(name, type):
        if re.search(r"[^\\\\\/\*\:\?\"\<\>\|]+.{}$".format(type), name):
            return name
        else:
            raise ValueError("invalid file name")


    @staticmethod
    def validate_existing_file(file):
        try:
            f = open(file, encoding='utf-8')
        except FileNotFoundError as e:
            raise FileNotFoundError(str(e))
        return file