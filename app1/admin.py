from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(InternationalCommunication)


class ContinueRateInline(admin.TabularInline):
    model = ContinueRate
    extra = 1


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    inlines = [ContinueRateInline]


class RoamingAddInfoInline(admin.TabularInline):
    model = RoamingAddInfo
    extra = 1


@admin.register(Roaming)
class RoamingAdmin(admin.ModelAdmin):
    inlines = [RoamingAddInfoInline]


class NextRoamingBusinessInline(admin.TabularInline):
    model = NextRoamingBusiness
    extra = 1


@admin.register(RoamingBusiness)
class Admin(admin.ModelAdmin):
    inlines = [NextRoamingBusinessInline]


class ContinueEquipmentInline(admin.TabularInline):
    model = ContinueEquipment
    extra = 1


@admin.register(Equipment)
class Admin(admin.ModelAdmin):
    inlines = [ContinueEquipmentInline]



