
"""Клас КОНТЕЙНЕР: ID, number (format: AB-12345), departure_city(enum),
 arrival_city (enum), departure_date, arrival_date, amount_of_items.
"""
from validation import Validation
from city import City
import json

class Container:
    def __init__(self, **kwargs):
        er = ""
        for prop, val in kwargs.items():
            try:
                setattr(self, prop, val)
            except ValueError as e:
                er+= "\n-- {}:\t".format(prop) + str(e)
        if len(er)>0:
            raise ValueError("Element Container can't be created: " + er)

    # id
    @property
    def ID(self):
        return self._ID

    @ID.setter
    @Validation.validate_id
    def ID(self, ID):
        self._ID = ID

    # number
    @property
    def number(self):
        return self._number

    @number.setter
    @Validation.validate_container_number
    def number(self, num):
        self._number = num

    #depart_city
    @property
    def departure_city(self):
        return self._departure_city
    @departure_city.setter
    @Validation.validate_city
    def departure_city(self, city):
        self._departure_city = city

    @property
    def arrival_city(self):
        return self._arrival_city
    @arrival_city.setter
    @Validation.validate_city
    def arrival_city(self, city):
        self._arrival_city = city

    @property
    def departure_date(self):
        return self._departure_date

    @departure_date.setter
    @Validation.validate_date
    @Validation.validate_later_date
    def departure_date(self, date):
        self._departure_date = date

    @property
    def arrival_date(self):
        return self._arrival_date

    @arrival_date.setter
    @Validation.validate_date
    @Validation.validate_later_date
    def arrival_date(self, date):
        self._arrival_date = date

    @property
    def amount_of_items(self):
        return self._amount_of_items
    @amount_of_items.setter
    @Validation.validate_non_negative_int
    def amount_of_items(self, num):
        self._amount_of_items = num

    #what will be used when print is called
    def __str__(self):
        d = self.props()
        data = "\n".join("{} : {}".format(prop, val) for prop, val in d.items())
        return "Container: \n" + data + "\n"

    def props(self):
        return dict((i[1:], str(getattr(self,i))) for i in self.__dict__.keys())
    @staticmethod
    def default_props():
        return ["ID","number","departure_city", "arrival_city", "departure_date", "arrival_date", "amount_of_items"]


    @Validation.validate_file_name("txt")
    def add_to_text_file(self, name):
        f = open(name, mode='a', encoding='utf-8')
        f.write("\n")
        f.write(str(str(self)))
        f.close()

    @Validation.validate_file_name("json")
    def add_to_json_file(self, name):
        try:
            f = open(name, mode='r+', encoding='utf-8')
            data = json.load(f)
            data.append(self.props())
            f.seek(0)
            json.dump(data, f, indent=4)
        except:
            f = open(name, "w")
            json.dump([self.props()], f, indent=4)
        f.close()
    @staticmethod
    def input_container(*args):
        d = dict((prop, input(prop + " : ")) for prop in args)
        return d
