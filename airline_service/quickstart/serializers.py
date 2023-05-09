from django.contrib.auth.models import User, Group
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PlaneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plane
        fields = ['url', 'plane_model', 'seats', 'size', 'company', 'age']


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AirlineCompany
        fields = ['url', 'name']


class FindSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FindFlight
        fields = ['url', 'depart', 'arrival']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookFlight
        fields = ['url', 'name', 'flight_id', 'seat_id', 'customer_id', 'email', 'phone']


class GpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GetPaymentMethod
        fields = ['url', 'code']


class PFBSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PayForBooking
        fields = ['url', 'price', 'number', 'method']


class FSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finalize
        fields = ['url', 'number', 'stamp']


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['url', 'number']


class CancelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cancel
        fields = ['url', 'number']


class SigninSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signin
        fields = ['url', 'email', 'password']


class SignupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Signup
        fields = ['url', 'name', 'username', 'email', 'password', 'card_number', 'bank_account', 'phone']


class DepositSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deposit
        fields = ['url', 'token', 'card_number', 'password']


class PaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pay
        fields = ['url', 'token', 'number', 'customer_id', 'price']

class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Balance
        fields = ['url', 'token']

class StatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stat
        fields = ['url', 'token']
