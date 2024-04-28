from django.urls import path
from .views import *


urlpatterns = [
     path('code_number/', CodeNumberViewSets.as_view({'get': 'list'}),
          name='code_number_list'),
     path('code_number/<int:pk>/', CodeNumberViewSets.as_view({'get': 'retrieve'}),
          name='code_number_detail'),
     path('status_number/', StatusNumberViewSets.as_view({'get': 'list'}),
          name='status_number_list'),
     path('status_number/<int:pk>/', StatusNumberViewSets.as_view({'get': 'retrieve'}),
          name='status_number_detail'),
     path('tariff_internetm2m/', TariffInternetM2MViewSets.as_view({'get': 'list'}),
          name='tariff_internetm2m_list'),
     path('tariff_internetm2m/<int:pk>/', TariffInternetM2MViewSets.as_view({'get': 'retrieve'}),
          name='tariff_internetm2m_detail'),
     path('next_tariff_internetm2m/', NextTariffInternetM2MViewSets.as_view({'get': 'list'}),
          name='next_tariff_internetm2m_list'),
     path('next_tariff_internetm2m/<int:pk>/', NextTariffInternetM2MViewSets.as_view({'get': 'retrieve'}),
          name='next_tariff_internetm2m_detail'),
     path('related_services/', RelatedServicesViewSets.as_view({'get': 'list'}),
          name='related_services_list'),
     path('related_services/<int:pk>/', RelatedServicesViewSets.as_view({'get': 'retrieve'}),
          name='related_services_detail'),
     path('advantages_m2m/', AdvantagesM2MViewSets.as_view({'get': 'list'}),
          name='advantages_m2m_list'),
     path('advantages_m2m/<int:pk>/', AdvantagesM2MViewSets.as_view({'get': 'retrieve'}),
          name='advantages_m2m_detail'),
     path('package/', PackageViewSets.as_view({'get': 'list'}),
          name='package_list'),
     path('package/<int:pk>/', PackageViewSets.as_view({'get': 'retrieve'}),
          name='package_detail'),
     path('questions/', QuestionsViewSets.as_view({'get': 'list'}),
          name='questions_list'),
     path('questions/<int:pk>/', QuestionsViewSets.as_view({'get': 'retrieve'}),
          name='questions_detail'),
]
