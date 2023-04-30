from django.core.exceptions import ValidationError
from .city.city import City


class ContainerValidation:
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
            raise ValidationError("invalid representation of city")
        return city

    @staticmethod
    def validate_later_date(date, later_date):
        if later_date < date:
            raise ValidationError("invalid date (impossible situation arrival before departure)")
        return date, later_date
