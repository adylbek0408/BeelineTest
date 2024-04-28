from rest_framework import viewsets
from serializers import *
from models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class CodeNumberViewSets(viewsets.ModelViewSet):
    queryset = CodeNumber.objects.all()
    serializer_class = CodeNumberSerializer


class StatusNumberViewSets(viewsets.ModelViewSet):
    queryset = StatusNumber.objects.all()
    serializer_class = StatusNumberSerializer


class TariffInternetM2MViewSets(viewsets.ModelViewSet):
    queryset = TariffInternetM2M.objects.all()
    serializer_class = TariffInternetM2MSerializer


class NextTariffInternetM2MViewSets(viewsets.ModelViewSet):
    queryset = NextTariffInternetM2M.objects.all()
    serializer_class = NextTariffInternetM2MSerializer


class RelatedServicesViewSets(viewsets.ModelViewSet):
    queryset = RelatedServices.objects.all()
    serializer_class = RelatedServicesSerializer


class AdvantagesM2MViewSets(viewsets.ModelViewSet):
    queryset = AdvantagesM2M.objects.all()
    serializer_class = AdvantagesM2MSerializer


class PackageViewSets(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer


class QuestionsViewSets(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

