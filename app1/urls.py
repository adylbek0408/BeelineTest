from django.urls import path
from .views import *


urlpatterns = [
    path('rate/', RateViewSets.as_view({'get': 'list'}),
         name='rate_list'),
    path('rate/<int:pk>/', RateViewSets.as_view({'get': 'retrieve'}),
         name='rate_detail'),
    path('continue_rate/', ContinueRateViewSets.as_view({'get': 'list'}),
         name='continue_rate_list'),
    path('continue_rate/<int:pk>/', ContinueRateViewSets.as_view({'get': 'retrieve'}),
         name='continue_rate_detail'),
    path('country/', CountryViewSets.as_view({'get': 'list'}),
         name='country_list'),
    path('country/<int:pk>/', CountryViewSets.as_view({'get': 'retrieve'}),
         name='country_detail'),
    path('roaming/', RoamingViewSets.as_view({'get': 'list'}),
         name='roaming_list'),
    path('roaming/<int:pk>/', RoamingViewSets.as_view({'get': 'retrieve'}),
         name='roaming_detail'),
    path('roaming_addinfo/', RoamingAddInfoViewSets.as_view({'get': 'list'}),
         name='roaming_addinfo_list'),
    path('roaming_addinfo/<int:pk>/', RoamingAddInfoViewSets.as_view({'get': 'retrieve'}),
         name='roaming_addinfo_detail'),
    path('roaming_business/', RoamingBusinessViewSets.as_view({'get': 'list'}),
         name='roaming_business_list'),
    path('roaming_business/<int:pk>/', RoamingBusinessViewSets.as_view({'get': 'retrieve'}),
         name='roaming_business_detail'),
    path('next_roaming_business/', NextRoamingBusinessViewSets.as_view({'get': 'list'}),
         name='next_roaming_business_list'),
    path('next_roaming_business/<int:pk>/', NextRoamingBusinessViewSets.as_view({'get': 'retrieve'}),
         name='next_roaming_business_detail'),
    path('international_communication/', InternationalCommunicationViewSets.as_view({'get': 'list'}),
         name='international_communication_list'),
    path('international_communication/<int:pk>/', InternationalCommunicationViewSets.as_view({'get': 'retrieve'}),
         name='international_communication_detail'),

    path('equipment/', EquipmentViewSets.as_view({'get': 'list'}),
         name='equipment_list'),
    path('equipment/<int:pk>/', EquipmentViewSets.as_view({'get': 'retrieve'}),
         name='equipment_detail'),

    path('continue_equipment/', ContinueEquipmentViewSets.as_view({'get': 'list'}),
         name='continue_equipment_list'),
    path('continue_equipment/<int:pk>/', ContinueEquipmentViewSets.as_view({'get': 'retrieve'}),
         name='continue_equipment_detail'),
]

