from booking_collection import BookingCollection
from booking import Booking
import sys
"""Варіант 2
Створити клас Booking, який містить такі поля
 1. Name (Тільки літери)
 2. NoOfPeople (1-10)
 3. StartTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)).
 4. EndTime (Клас Time, що містить 2 поля: hour (00 - 23), minute (00 - 59)). Min: StartTime. 
 5. Price (Число з 2 знаками після коми)
Створити такі методи:
 1. Зчитати масив (клас для роботи з масивом екземплярів класу Booking) Booking з файла (1)
 2. Додати новий Booking. На одну і ту саму годину одночасно може бути заброньовано 15 місць. Наприклад, #1: 10 людей 10:00 - 11:00, #2: 6 людей 10:00 - 10:30 забронювати неможливо, оскільки на 10:00 забронювати можна лише 15 людей. Мінімальна тривалість резервації - 30 хв, максимальна - 1 год 30 хв. (3)
 3. Додати валідацію на поля Name, NoOfPeople, StartTime, EndTime, Price. (2)
 4. Визначити годину, на яку є найбільше замовлень. Якщо таких декілька - вивести всі години. (2)
 5. Кожен 2 доданий Booking ціна за день автоматично піднімається на 10.00. (1.5)
 6. Вивести всі Bookings на екран (0.5)"""
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