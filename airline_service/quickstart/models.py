from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Plane(models.Model):
    plane_model = models.CharField(max_length=100)
    seats = models.IntegerField(max_length=500)
    age = models.IntegerField(max_length=100)
    company = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.plane_model


class AirlineCompany(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FindFlight(models.Model):
    depart = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    depart_time = models.DateTimeField


class BookFlight(models.Model):
    flight_id = models.CharField(max_length=100)
    seat_id = models.IntegerField(max_length=500)
    name = models.CharField(max_length=100)
    customer_id = models.IntegerField(max_length=500)
    email = models.CharField(max_length=250)
    phone = models.IntegerField(max_length=500)


class GetPaymentMethod(models.Model):
    code = models.IntegerField(max_length=500)


class PayForBooking(models.Model):
    price = models.IntegerField(max_length=500)
    number = models.CharField(max_length=500)
    method = models.CharField(max_length=500)


class Finalize(models.Model):
    number = models.CharField(max_length=500)
    stamp = models.CharField(max_length=500)


class Status(models.Model):
    number = models.CharField(max_length=500)


class Cancel(models.Model):
    number = models.CharField(max_length=500)


class Signin(models.Model):
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)


class Signup(models.Model):
    name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    card_number = models.IntegerField(max_length=500)
    phone = models.IntegerField(max_length=500)
    bank_account = models.IntegerField(max_length=500)


class Deposit(models.Model):
    token = models.CharField(max_length=500)
    card_number = models.IntegerField(max_length=500)
    password = models.CharField(max_length=500)


class Pay(models.Model):
    token = models.CharField(max_length=500)
    number = models.IntegerField(max_length=500)
    customer_id = models.IntegerField(max_length=500)
    price = models.IntegerField(max_length=500)


class Balance(models.Model):
    token = models.CharField(max_length=500)


class Stat(models.Model):
    token = models.CharField(max_length=500)
