from rest_framework import serializers
from .models import *


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class ContinueRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinueRate
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RoamingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roaming
        fields = '__all__'


class RoamingAddInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoamingAddInfo
        fields = '__all__'


class RoamingBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoamingBusiness
        fields = '__all__'


class NextRoamingBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextRoamingBusiness
        fields = '__all__'


class InternationalCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalCommunication
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class ContinueEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContinueEquipment
        fields = '__all__'
