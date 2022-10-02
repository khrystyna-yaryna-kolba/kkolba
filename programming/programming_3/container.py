
"""Клас КОНТЕЙНЕР: ID, number (format: AB-12345), departure_city(enum),
 arrival_city (enum), departure_date, arrival_date, amount_of_items.
"""
from validation import Validation
from city import City
import json

class Container:
    def __init__(self, **kwargs):
        for prop, val in kwargs.items():
            setattr(self, prop, val)
    # id
    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        id = Validation.validate_id(ID)
        self._ID = id

    # number
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, num):
        number = Validation.validate_container_number(num)
        self._number = number

    #depart_city
    @property
    def departure_city(self):
        return self._departure_city
    @departure_city.setter
    def departure_city(self, city):
        city = Validation.validate_city(city)
        self._departure_city = city

    @property
    def arrival_city(self):
        return self._arrival_city
    @arrival_city.setter
    def arrival_city(self, city):
        city = Validation.validate_city(city)
        self._arrival_city = city

    @property
    def departure_date(self):
        return self._departure_date
    @departure_date.setter
    def departure_date(self, date):
        date = Validation.validate_date(date)
        if hasattr(self, "_arrival_date"):
            Validation.validate_later_date(date, self._arrival_date)
        self._departure_date = date

    @property
    def arrival_date(self):
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, date):
        date = Validation.validate_date(date)
        if hasattr(self, "_departure_date"):
            date = Validation.validate_later_date(self._departure_date, date)
        self._arrival_date = date

    @property
    def amount_of_items(self):
        return self._amount_of_items
    @amount_of_items.setter
    def amount_of_items(self, num):
        num = Validation.validate_non_negative_int(num)
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
    def add_to_text_file(self, name):
        name = Validation.validate_file_name(name, "txt")
        f = open(name, mode='a', encoding='utf-8')
        f.write("\n")
        f.write(str(str(self)))
        f.close()
    def add_to_json_file(self, name):
        name = Validation.validate_file_name(name, "json")
        f = open(name, mode='r+', encoding='utf-8')
        data = json.load(f)
        data.append(self.props())
        f.seek(0)
        json.dump(data, f, indent=4)
        f.close()
    @staticmethod
    def input_container(*args):
        d = dict((prop, input(prop + " : ")) for prop in args)
        return d



#cont = Container(**Container.input_container("number", "amount_of_items"))
#cont.departure_city="LONDON"
#cont.arrival_date="27.09.2022"
#print(cont)