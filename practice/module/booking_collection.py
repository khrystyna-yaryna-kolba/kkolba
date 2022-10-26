from validation_booking_collection import ValidationBookingCollection
import json
from booking import Booking


class BookingCollection:
    ADD = 1
    def __init__(self, *argv):
        self._collection = list(argv)

    def __getitem__(self, item):
        return self._collection[item]

    def __str__(self):
        return "\n".join([str(i) for i in self._collection])

    def __len__(self):
        return len(self._collection)

    @ValidationBookingCollection.validate_new_booking
    def add_element(self, elem):
        self._collection.append(elem)

    @ValidationBookingCollection.validate_file_name("json")
    @ValidationBookingCollection.validate_existing_file
    def read_json_file(self, f):
        self._collection = []
        file = json.load(f)
        for i, booking in enumerate(file):
            try:
                self.add_element(Booking(**booking))
            except ValueError as e:
                print(str(e), "\nin {} object in file".format(i))
                continue
        f.close()

    def top_hour(self):
        top_hours = {}
        for i in range(len(self._collection)):
            top_hours[str(self[i].StartTime)] = top_hours[str(self[i].StartTime)] + 1 if str(self[i].StartTime) in top_hours else 1
        max_bookings = max(top_hours, key=top_hours.get)
        print()
        res = []
        for i in top_hours.keys():
            if top_hours[i] == top_hours[max_bookings]:
                res.append(i)
        return res, top_hours[max_bookings]
