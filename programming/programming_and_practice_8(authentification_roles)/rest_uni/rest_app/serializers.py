from rest_framework import serializers
from .models import Containers, UserData, ContainerOrder
from .city.city import City
import re
from datetime import datetime
from .serializers_validation import SerializerValidation

class ContainerSerializer(serializers.ModelSerializer):
    ID = serializers.IntegerField(min_value=0)
    number = serializers.CharField(max_length=8)
    departure_city = serializers.CharField(max_length=50)
    arrival_city = serializers.CharField(max_length=50)
    departure_date = serializers.DateField()
    arrival_date = serializers.DateField()
    amount_of_items = serializers.IntegerField(min_value=0)
    """
    ContainerSerializer class that is responsible for transforming json data to our Containers Model
    and vice-versa
    - > responsible for validating raw data (json) (creates Containers Model object using validated data)
    """
    def validate_number(self, num):
        num = SerializerValidation.validate_number(num)
        return num

    def validate_ID(self, id):
        id = SerializerValidation.validate_non_negative_int(id)
        return id

    def validate_departure_city(self, city):
        city = SerializerValidation.validate_city(city)
        return city

    def validate_arrival_city(self, city):
        city = SerializerValidation.validate_city(city)
        return city

    def validate_amount_of_items(self, val):
        val = SerializerValidation.validate_non_negative_int(val)
        return val

    def validate_arrival_date(self, date):
        dep = SerializerValidation.validate_date(self.initial_data["departure_date"])
        dep, date = SerializerValidation.validate_later_date(dep, date)
        return date

    # this method is invoked when .save() is called and self.instance is None
    def create(self, validated_data):
        return Containers.objects.create(**validated_data)

    # this method is invoked when .save() is called but self.instance is not None
    def update(self, instance, validated_data):
        # if we want to change id we can`t do it directly
        # but, we can just delete element with current id and create new
        if int(instance.ID) != int(validated_data["ID"]):
            duplicat = Containers.objects.filter(ID=validated_data["ID"])
            if duplicat:
                return instance
            instance.delete()
            instance = Containers(**validated_data)
            instance.save()
            return instance
        instance.ID = validated_data["ID"]
        instance.number = validated_data["number"]
        instance.departure_city = validated_data["departure_city"]
        instance.arrival_city = validated_data["arrival_city"]
        instance.departure_date = validated_data["departure_date"]
        instance.arrival_date = validated_data["arrival_date"]
        instance.amount_of_items = validated_data["amount_of_items"]
        instance.save()
        return instance

    class Meta:
        model = Containers
        fields = ('__all__')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "first_name", "last_name", "password"]

    def validate_password(self, p):
        p = SerializerValidation.validate_password(p)
        return p

    def validate_first_name(self, n):
        n = SerializerValidation.validate_name(n)
        return n

    def validate_last_name(self, n):
        n = SerializerValidation.validate_name(n)
        return n

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       first_name=validated_data['first_name'],last_name=validated_data['last_name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ContainerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerOrder
        fields = '__all__'

class ContainerOrderForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContainerOrder
        fields = ["container_id", "date", "amount"]


