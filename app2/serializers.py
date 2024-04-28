from rest_framework import serializers
from models import *


class CodeNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeNumber
        fields = '__all__'


class StatusNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusNumber
        fields = '__all__'


class TariffInternetM2MSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffInternetM2M
        fields = '__all__'


class NextTariffInternetM2MSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextTariffInternetM2M
        fields = '__all__'


class RelatedServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatedServices
        fields = '__all__'


class AdvantagesM2MSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvantagesM2M
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'