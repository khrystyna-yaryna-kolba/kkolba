from class_time import Time
from datetime import datetime
import re
MAX_PEOPLE = 10
class ValidationBooking:
    @staticmethod
    def validate_num_of_people(func):
        def inner(f, n):
            try:
                n = int(n)
                if n < 0 or n > MAX_PEOPLE:
                    raise ValueError("num of people should be in range 0-{}".format(MAX_PEOPLE))
            except ValueError:
                raise ValueError("num of people should be a number")
            return func(f, n)
        return inner

    @staticmethod
    def validate_name(func):
        def inner(f, n):
            if not re.search(r"[a-zA-z]+", n):
                raise ValueError("invalid format of booking name")
            return func(f,n)
        return inner

    @staticmethod
    def validate_price(func):
        def inner(f, n):
            if not re.search(r"[0-9]+\.[0-9]{2}$", str(n)):
                raise ValueError("invalid price")
            return func(f,n)
        return inner

    @staticmethod
    def validate_start_time(func):
        def inner(f, time):
            try:
                h = int(time[:2])
                m = int(time[3:])
                time = Time(h,m)
            except ValueError as e:
                raise ValueError(str(e))
            return func(f, time)
        return inner

    @staticmethod
    def validate_end_time(func):
        def inner(f, time):
            try:
                h = int(time[:2])
                m = int(time[3:])
                time = Time(h, m)
                if time < f.StartTime:
                    raise ValueError("end time can't be earlier that start time")
            except ValueError as e:
                raise ValueError(str(e))
            return func(f, time)
        return inner
