from rest_framework import serializers
import re
from datetime import datetime
from .city.city import City


class SerializerValidation:
    @staticmethod
    def validate_password(p):
        pat = re.compile(r"(?=.*[a-z])(?=.*[A-Z]).{8,}$")
        if not re.search(pat, p):
            raise serializers.ValidationError("Password should contain at least one uppercase letter, one lowercase letter and be "
                                              "at least 8 symbols long")
        return p

    @staticmethod
    def validate_name(name):
        if not re.search(r"^[A-Za-z]{2,}$", name):
            raise serializers.ValidationError("shoud contain only lowercase or uppercase letters and be at least 2 "
                                              "symbols long")
        return name

    @staticmethod
    def validate_number(num):
        if not re.search(r"^[A-Z]{2}-[0-9]{5}$", num):
            raise serializers.ValidationError("invalid format of container number")
        return num

    @staticmethod
    def validate_city(city):
        try:
            city = list(city)
            for i, c in enumerate(city):
                if c == " ":
                    city[i] = "_"
                city[i] = city[i].upper()
            city = "".join(city)
            city = City[city]
        except KeyError:
            raise serializers.ValidationError("invalid representation of city")
        return city

    @staticmethod
    def validate_non_negative_int(val):
        try:
            n = int(val)
            if n < 0:
                raise serializers.ValidationError("number cannot be negative")
        except ValueError:
            raise serializers.ValidationError("number must be a non negative integer")
        return n

    @staticmethod
    def validate_date(date):
        try:
            d = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise serializers.ValidationError("invalid date")
        return d

    @staticmethod
    def validate_later_date(date, later_date):
        if later_date < date:
            raise serializers.ValidationError("invalid date (impossible situation arrival before departure)")
        return date, later_date
