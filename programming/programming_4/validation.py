from datetime import datetime
import re
from city import City


class Validation:
    # id should be consisted of positive integer (or 0) but also can begin with zero and have different length
    # means should contain only digits
    @staticmethod
    def validate_id(func):
        def validate_id_inner(container, val):
            for i in val:
                if not i.isdigit():
                    raise ValueError("invalid id (valid should contain digits only)")
            return func(container, val)
        return validate_id_inner

    @staticmethod
    def validate_date(func):
        def validate_date_inner(cont, da):
            try:
                d = datetime.strptime(da, "%Y-%m-%d").date()
            except ValueError:
                raise ValueError("invalid date")
            return func(cont, d)
        return validate_date_inner

    @staticmethod
    def validate_later_date(func):
        def validate_later_date_inner(dep, second):
            if hasattr(dep, "_departure_date"):
                if dep.departure_date > second:
                    raise ValueError("invalid date (impossible situation departure after arrival)")
            elif hasattr(dep, "_arrival_date"):
                if dep.arrival_date < second:
                    raise ValueError("invalid date (impossible situation arrival before departure)")
            return func(dep, second)
        return validate_later_date_inner

    @staticmethod
    def validate_non_negative_int(func):
        def validate_non_negative_int_inner(cont, val):
            try:
                n = int(val)
                if n < 0:
                    raise ValueError("number cannot be negative")
            except ValueError:
                raise ValueError("number must be a non negative integer")
            return func(cont, n)
        return validate_non_negative_int_inner

    @staticmethod
    def validate_container_number(func):
        def validate_container_number_inner(cont, number):
            if not re.search(r"^[A-Z]{2}-[0-9]{5}$", number):
                raise ValueError("invalid format of container number")
            return func(cont, number)
        return validate_container_number_inner

    @staticmethod
    def validate_city(func):
        def validate_city_inner(cont, city):
            try:
                city = list(city)
                for i, c in enumerate(city):
                    if c == " ":
                        city[i] = "_"
                    city[i] = city[i].upper()
                city = "".join(city)
                city = City[city]
            except KeyError:
                raise ValueError("invalid representation of city")
            return func(cont, city)
        return validate_city_inner

    @staticmethod
    def validate_file_name(type):
        def validate_file_name_wrap(func):
            def validate_file_name_inner(cont, name):
                if not re.search(r"[^\\\\\/\*\:\?\"\<\>\|]+.{}$".format(type), name):
                    raise ValueError("invalid file name")
                return func(cont, name)

            return validate_file_name_inner
        return validate_file_name_wrap

    @staticmethod
    def validate_edit_id(func):
        def validate_edit_id_inner(*argv):
            if argv[1] in argv[0].get_ids():
                raise KeyError("ID {} is not unique. Can`t edit".format(argv[1]))
            else:
                return func(*argv)

        return validate_edit_id_inner

    @staticmethod
    def validate_existing_file(func):
        def validate_existing_file_inner(cont, f):
            try:
                f = open(f, encoding='utf-8')
            except FileNotFoundError as e:
                raise FileNotFoundError(str(e))
            return func(cont, f)
        return validate_existing_file_inner

    @staticmethod
    def validate_collection_id(func):
        def validate_collection_id_inner(*argv):
            if not argv[1] in argv[0].get_ids():
                raise KeyError("element with id {} doesn`t exist in collection".format(argv[1]))
            else:
                return func(*argv)
        return validate_collection_id_inner

    @staticmethod
    def validate_new_id(func):
        def validate_new_id_inner(col, el):
            if el.ID in col.get_ids():
                raise KeyError("ID {} is not unique".format(el.ID))
            else:
                return func(col, el)

        return validate_new_id_inner


    @staticmethod
    def validate_default_property(default, pos):
        def validate_default_property_wrap(func):
            def validate_default_property_inner(*argv):
                if not argv[pos] in default:
                    raise AttributeError("property {} is not valid, action was not completed".format(argv[pos]))
                return func(*argv)
            return validate_default_property_inner
        return validate_default_property_wrap

