from django.db import models
# from django.core.exceptions import ValidationError
# Create your models here.
"""Клас КОНТЕЙНЕР: ID, number (format: AB-12345), departure_city(enum),
 arrival_city (enum), departure_date, arrival_date, amount_of_items.
"""


class Containers(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    number = models.CharField(max_length=8)
    departure_city = models.CharField(max_length=50)
    arrival_city = models.CharField(max_length=50)
    departure_date = models.DateField()
    arrival_date = models.DateField()
    amount_of_items = models.PositiveIntegerField()

    def __str__(self):
        d = self.props()
        data = "\n".join("{} : {}".format(prop, val) for prop, val in d.items())
        return "Container: \n" + data + "\n"

    @staticmethod
    def search(sort_by, sort_type, s):
        result = Containers.objects.all()
        containers = []
        for i in result:
            if s is None or i.search_in_record(s):
                containers.append(i)

        containers = Containers.sort(containers, sorting_attr=sort_by, sort_type = sort_type)
        return containers

    @staticmethod
    def sort(lis, sorting_attr = "number", sort_type = "asc"):
        # function helper to lambda
        reverse = (sort_type == "desc")
        sorting_attr = "number" if sorting_attr is None or sorting_attr not in Containers.default_props() else sorting_attr
        def get_attr(x):
            attr = getattr(x, sorting_attr)
            if isinstance(attr, str):
                return attr.lower()
            else:
                return attr
        return sorted(lis, key=lambda x: get_attr(x), reverse=reverse)

    @staticmethod
    def default_props():
        return ["ID","number","departure_city", "arrival_city", "departure_date", "arrival_date", "amount_of_items"]

    def json_data(self):
        return dict((i, str(getattr(self,i))) for i in self.__dict__.keys() if i != "_state")

    def search_in_record(self, s):
        for i in self.__dict__.values():
            if str(i).find(s) != -1:
                return True
        return False