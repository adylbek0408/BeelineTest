from rest_framework import viewsets
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class RateViewSets(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_archive']


class ContinueRateViewSets(viewsets.ModelViewSet):
    queryset = ContinueRate.objects.all()
    serializer_class = ContinueRateSerializer


class CountryViewSets(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    filter_backends = [SearchFilter]
    search_fields = ['country']


class RoamingViewSets(viewsets.ModelViewSet):
    queryset = Roaming.objects.all()
    serializer_class = RoamingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country_roaming']


class RoamingAddInfoViewSets(viewsets.ModelViewSet):
    queryset = RoamingAddInfo.objects.all()
    serializer_class = RoamingAddInfoSerializer


class RoamingBusinessViewSets(viewsets.ModelViewSet):
    queryset = RoamingBusiness.objects.all()
    serializer_class = RoamingBusinessSerializer


class NextRoamingBusinessViewSets(viewsets.ModelViewSet):
    queryset = NextRoamingBusiness.objects.all()
    serializer_class = NextRoamingBusinessSerializer


class InternationalCommunicationViewSets(viewsets.ModelViewSet):
    queryset = InternationalCommunication.objects.all()
    serializer_class = InternationalCommunicationSerializer


class EquipmentViewSets(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer


class ContinueEquipmentViewSets(viewsets.ModelViewSet):
    queryset = ContinueEquipment.objects.all()
    serializer_class = ContinueEquipmentSerializer


