from django.contrib import admin
from .models import *


admin.site.register(RelatedServices)
admin.site.register(AdvantagesM2M)
admin.site.register(Package)
admin.site.register(Questions)


class StatusNumberInline(admin.TabularInline):
    model = StatusNumber
    extra = 1


@admin.register(CodeNumber)
class StatusNumberAdmin(admin.ModelAdmin):
    inlines = [StatusNumberInline]


class NextTariffInternetM2MInline(admin.TabularInline):
    model = NextTariffInternetM2M
    extra = 1


@admin.register(TariffInternetM2M)
class TariffInternetM2MAdmin(admin.ModelAdmin):
    inlines = [NextTariffInternetM2MInline]

