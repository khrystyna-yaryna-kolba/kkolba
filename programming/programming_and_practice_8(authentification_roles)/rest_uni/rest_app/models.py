from datetime import datetime
from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from .models_validation import ContainerValidation
# Create your models here.
"""Клас КОНТЕЙНЕР: ID, number (format: AB-12345), departure_city(enum),
 arrival_city (enum), departure_date, arrival_date, amount_of_items.
"""
class Containers(models.Model):
    ID = models.PositiveIntegerField(primary_key=True)
    number = models.CharField(max_length=8, validators=[RegexValidator(regex=r"^[A-Z]{2}-[0-9]{5}$", message="The invalid container number", code="invalid_number")])
    departure_city = models.CharField(max_length=50, validators=[ContainerValidation.validate_city])
    arrival_city = models.CharField(max_length=50, validators=[ContainerValidation.validate_city])
    departure_date = models.DateField()
    arrival_date = models.DateField()
    amount_of_items = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    def __str__(self):
        d = self.props()
        data = "\n".join("{} : {}".format(prop, val) for prop, val in d.items())
        return "Container: \n" + data + "\n"

    def clean(self, *args, **kwargs):
        ContainerValidation.validate_later_date(self.departure_date, self.arrival_date)
        return super().clean(*args, **kwargs)


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

    def props(self):
        return dict((i[:], str(getattr(self, i))) for i in self.default_props())

    def json_data(self):
        return dict((i, str(getattr(self,i))) for i in self.__dict__.keys() if i != "_state")

    def search_in_record(self, s):
        for i in self.__dict__.values():
            if str(i).find(s) != -1:
                return True
        return False


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, first_name, last_name, email, password=None, **extra_fields):
        if not email or not first_name or not last_name:
            raise ValueError('All fields are Required')
        user = self.model(email=self.normalize_email(email), first_name = first_name, last_name = last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(first_name, last_name, email, password, **extra_fields)


class UserData(AbstractUser):
    username = None
    last_login =None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name

    def is_admin(self):
        return self.is_staff


class ContainerOrder(models.Model):
    user_id = models.ForeignKey(UserData, on_delete=models.CASCADE)
    container_id = models.ForeignKey(Containers, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        d = self.props()
        data = "\n".join("{} : {}".format(prop, val) for prop, val in d.items())
        return "ContainerOrder: \n" + data + "\n"

    @staticmethod
    def default_props():
        return ["id", "user_id", "container_id", "amount", "date"]

    def props(self):
        return dict((i[:], str(getattr(self, i))) for i in self.default_props())