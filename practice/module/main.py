from booking_collection import BookingCollection
from booking import Booking
import sys
def menu():
    f_bookings = BookingCollection()
    while True:
        try:
            choice = input("enter your choice \n 1 - read from file"
                       "\n 2 - add new booking to current collection \n 3 - find top hours with max bookings \n 4 - print "
                           "current collection"
                       "\n 5 - exit \n")
            if choice=="1":
                name = input("Input file name to read from(.json): \n")
                f_bookings.read_json_file(name)
            elif choice == "2":
                el = Booking(**Booking.input_container())
                f_bookings.add_element(el)
            elif choice == "3":
                res, hour = f_bookings.top_hour()
                print("Hours: ", res)
                print("max bookings on the same hour: ", hour)

            elif choice=="4":
                print(f_bookings)
        except:
            e = sys.exc_info()[1]
            print("Error: ", str(e))
            continue

        if choice == "5":
            exit()
        else:
            continue

def write_to_file(name, data):
    name = validate_file_name(name, "txt")
    f = open(name, mode='a', encoding='utf-8')
    f.write(", ".join(data))
    f.close()

def validate_file_name(name, type):
    import re
    if not re.search(r"[^\\\\\/\*\:\?\"\<\>\|]+.{}$".format(type), name):
        raise ValueError("invalid file name")
    return name


menu()