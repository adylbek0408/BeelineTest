from django.db import models
from ckeditor.fields import RichTextField


class Rate(models.Model):
    """Тариф"""
    title = models.CharField(max_length=50, verbose_name='Название', null=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описания')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')
    gigabytes = RichTextField(verbose_name='Гигабайты', null=True)
    price = models.IntegerField(verbose_name='Цена', null=True, blank=True)
    it_work = models.CharField(max_length=30, verbose_name='Недели Месяцы', null=True, blank=True)
    is_archive = models.BooleanField(default=False, verbose_name='Архивировать', null=True)
    international_challenges = models.TextField(null=True, blank=True, verbose_name='Международные вызовы')
    ussd_code = models.CharField(max_length=10, verbose_name=' USSD-код: Подключении', null=True)

    def __str__(self):
        return self.title


class ContinueRate(models.Model):
    """Продолжения Тарифа"""
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE, related_name='continue_rate', verbose_name='Тариф', null=True)
    calls_sms = (
        ('Обычный SMS', 'usual_call'),
        ('Обычный Звонки', 'usual_sms'),
        ('Доп. Звонки', 'call'),
        ('Доп. SMS', 'sms'),
    )
    calls_sms = models.CharField(max_length=100, choices=calls_sms, verbose_name='Звонки и SMS', null=True)
    rich_rate = RichTextField(verbose_name='Звонки или SMS', null=True)

    def __str__(self):
        return f"   {self.calls_sms} | {self.rate}"


class Country(models.Model):
    country = models.CharField(max_length=30, verbose_name='Страна', null=True)
    image = models.ImageField(verbose_name='Флаг Страны', null=True)

    def __str__(self):
        return self.country


class Roaming(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', null=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описания')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')
    gigabytes = RichTextField(verbose_name='Гигабайты', null=True)
    minutes = RichTextField(verbose_name='Звонки', null=True)
    price = models.IntegerField(verbose_name='Цена', null=True)
    it_works = models.CharField(max_length=50, verbose_name='Действует', null=True)
    country_roaming = models.ManyToManyField(Country, verbose_name='Стран Действия', null=True)
    ussd_code = models.CharField(max_length=10, verbose_name='USSD-код: Подключении', null=True)

    def __str__(self):
        return self.title


class RoamingAddInfo(models.Model):
    roaming = models.ForeignKey(Roaming, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=54, verbose_name='Название', null=True)
    description = RichTextField(verbose_name='Описания подробности', null=True)

    def __str__(self):
        return self.name


class RoamingBusiness(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', null=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описания')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')
    gigabytes = RichTextField(verbose_name='Гигабайты', null=True)
    minutes = RichTextField(verbose_name='Звонки', null=True)
    country_roaming_business = models.ManyToManyField(Country, verbose_name='Стран Действия', null=True)
    ussd_code = models.CharField(max_length=10, verbose_name='USSD-код: Подключении', null=True)

    def __str__(self):
        return self.title


class NextRoamingBusiness(models.Model):
    roaming_business = models.ForeignKey(RoamingBusiness, on_delete=models.CASCADE, related_name='sequels_roaming',
                                         verbose_name='Роуминг Бизнес', null=True)
    call_sms_balance = (
        ('Исходящие звонки в роуминге', 'call'),
        ('Исходящие SMS в роуминге', 'sms'),
        ('При недостатке средств на балансе:', 'balance'),
    )
    call_sms_balance = models.CharField(max_length=100, choices=call_sms_balance, verbose_name='Звонки SMS Баланс', null=True)
    rich_roaming_business = RichTextField(verbose_name='Звонки или SMS или Баланс', null=True)

    def __str__(self):
        return f"{self.call_sms_balance} {self.roaming_business}"


class InternationalCommunication(models.Model):
    """Международная связь"""
    title = models.CharField(max_length=50, verbose_name='Название', null=True)
    description = models.TextField(null=True, blank=True, verbose_name='Описания')
    image = models.ImageField(null=True, blank=True, verbose_name='Картинка')
    calls = RichTextField(verbose_name='Звонки', null=True)
    sms = RichTextField(verbose_name='SMS', null=True)
    it_works = models.CharField(max_length=40, verbose_name='Действует', null=True)
    price = models.IntegerField(verbose_name='Цена', null=True)
    country_international_comm = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна', null=True)
    ussd_code = models.CharField(max_length=10, verbose_name='USSD-код: Подключении', null=True)

    def __str__(self):
        return self.title


class Equipment(models.Model):
    """Оборудование"""
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    full_description = models.TextField(null=True)
    video = models.FileField(null=True)


class ContinueEquipment(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True)
    var_tech_spec = (
        ('Варианты приобретения', 'purchase options'),
        ('Технические характеристики', 'technical specifications'),
    )
    var_tech_spec = models.CharField(max_length=100, choices=var_tech_spec, verbose_name='Вар оплаты или Тех хар', null=True)
    text = models.CharField(max_length=155, null=True)
    technical = models.CharField(max_length=100, null=True)
