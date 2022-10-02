from datetime import datetime
import re
from city import City

class Validation:
    @staticmethod
    def validate_int(val):
        try:
            n = int(val)
        except ValueError:
            raise ValueError("number must be an integer")
        return n
    #id should be consisted of positive integer (or 0) but also can begin with zero and have different length
    #means should contain only digits
    @staticmethod
    def validate_id(val):
        try:
            for i in val:
                if not i.isdigit():
                    raise ValueError("invalid id (valid should contain digits only)")
        except ValueError:
            raise ValueError("invalid id (valid should contain digits only)")
        return val
    @staticmethod
    def validate_date(d):
        try:
            d = datetime.strptime(d, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("invalid date")
        return d

    @staticmethod
    def validate_later_date(first, second):
        if first>second:
            raise ValueError("invalid date (impossible situation)")
        return second
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
    def validate_container_number(number):
        if re.search(r"^[A-Z]{2}-[0-9]{5}$", number):
            return number
        else:
            raise ValueError("invalid format of container number")

    @staticmethod
    def validate_city(city):
        try:
            city = list(city)
            for i, c in enumerate(city):
                if c==" ":
                    city[i]="_"
                city[i]=city[i].upper()
            city = "".join(city)
            city = City[city]
        except KeyError:
            raise ValueError("invalid representation of city")
        return city
    @staticmethod
    def validate_file_name(name, type):
        if re.search(r"[^\\\\\/\*\:\?\"\<\>\|]+.{}$".format(type), name):
            return name
        else:
            raise ValueError("invalid file name")


    @staticmethod
    def if_id_exist(collection, id):
        if id in collection.get_ids():
            return True
        else:
            return False
