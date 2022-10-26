from validation_time import ValidationTime
class Time:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @property
    def hour(self):
        return self._hour

    @hour.setter
    @ValidationTime.validate_non_negative_int
    @ValidationTime.validate_val_in_range(0,23)
    def hour(self, h):
        self._hour = h

    @property
    def minute(self):
        return self._minute

    @minute.setter
    @ValidationTime.validate_non_negative_int
    @ValidationTime.validate_val_in_range(0, 59)
    def minute(self, m):
        self._minute = m

    def __lt__(self, other):
        if self.hour != other.hour:
            return self.hour < other.hour
        else:
            return self.minute < other.minute

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __str__(self):
        h = str(self.hour) if self.hour>9 else "0{}".format(self.hour)
        m = str(self.minute) if self.minute > 9 else "0{}".format(self.minute)
        return "{}:{}".format(h, m)

    def minutes_dif(self, other):
        if self < other:
            hours = other.hour - self.hour
            if other.minute < self.minute:
                minutes = 60 + other.minute - self.minute
                hours = hours - 1
            else:
                minutes = other.minute - self.minute
            return hours*60 + minutes
        elif other < self:
            hours = self.hour - other.hour
            if other.minute > self.minute:
                minutes = 60 + self.minute - other.minute
                hours = hours - 1
            else:
                minutes = self.minute - other.minute
            return hours * 60 + minutes
        else:
            return 0
        #elif self.hour == other.hour:
         #   hours = 0
         #   if other.minute > self.minute:
         #       minutes = other.minute - self.minute
         #   else:
          #      minutes = self.minute - other.minute
          #  return hours * 60 + minutes

"""test1 = Time(22,3)
test2 = Time(22,3)
print(test1.minutes_dif(test2))"""