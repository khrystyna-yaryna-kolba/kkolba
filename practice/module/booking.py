from validation_booking import ValidationBooking
from datetime import datetime

class Booking:
    def __init__(self,  **kwargs):
        er = ""
        for prop, val in kwargs.items():
            try:
                setattr(self, prop, val)
            except ValueError as e:
                er += "\n-- {}:\t".format(prop) + str(e)
        if len(er) > 0:
            raise ValueError("Element Booking can't be created: " + er)

    @property
    def Name(self):
        return self._Name

    @Name.setter
    @ValidationBooking.validate_name
    def Name(self, c):
        self._Name = c

    @property
    def NoOfPeople(self):
        return self._NoOfPeople

    @NoOfPeople.setter
    @ValidationBooking.validate_num_of_people
    def NoOfPeople(self, n):
        self._NoOfPeople = n

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    @ValidationBooking.validate_start_time
    def StartTime(self, st):
        self._StartTime = st

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    @ValidationBooking.validate_end_time
    def EndTime(self, et):
        self._EndTime = et

    @property
    def Price(self):
        return self._Price

    @Price.setter
    @ValidationBooking.validate_price
    def Price(self, d):
        self._Price = d

    def __str__(self):
        d = self.props()
        d["Price"] = "{:.2f}".format(float(d["Price"]))
        data = "\n".join("{} : {}".format(prop, val) for prop, val in d.items())
        return "Booking: \n" + data + "\n"

    def props(self):
        d = dict((i[1:], str(getattr(self, i[1:]))) for i in self.__dict__.keys())
        return d

    @staticmethod
    def default_props():
        return ["Name", "NoOfPeople", "StartTime", "EndTime", "Price"]

    @staticmethod
    def input_container():
        props = Booking.default_props()
        d = dict((prop, input(prop + " : ")) for prop in props)
        return d
