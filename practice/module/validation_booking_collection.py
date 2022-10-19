import re
class ValidationBookingCollection:
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
    def validate_existing_file(func):
        def validate_existing_file_inner(cont, f):
            try:
                f = open(f, encoding='utf-8')
            except FileNotFoundError as e:
                raise FileNotFoundError(str(e))
            return func(cont, f)
        return validate_existing_file_inner

    @staticmethod
    def validate_new_booking(func):
        MAX_MINUTES = 90
        MIN_MINUTES = 30
        MAX_PEOPLE = 15
        def inner(col, new_el):
            #reservation time validation
            if new_el.StartTime.minutes_dif(new_el.EndTime) > MAX_MINUTES or new_el.StartTime.minutes_dif(new_el.EndTime) <MIN_MINUTES:
                raise ValueError("can't register booking with reservation time less than {} or more than {} minutes".format(MIN_MINUTES,MAX_MINUTES))
            # max people validation
            tot_people = 0
            for i in range(len(col)):
                if col[i].StartTime == new_el.StartTime:
                    tot_people += col[i].NoOfPeople
            if tot_people + new_el.NoOfPeople > MAX_PEOPLE:
                raise ValueError("can't register more than {} at the same time".format(MAX_PEOPLE))

            #automatic raise
            if col.ADD == 1:
                col.ADD = 2
            else:
                new_el.Price = round(float(new_el.Price) + 10.00, 2)
                col.ADD = 1
            return func(col, new_el)

        return inner
