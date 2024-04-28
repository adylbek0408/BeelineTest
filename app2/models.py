from django.db import models
from ckeditor.fields import RichTextField


class CodeNumber(models.Model):
    code = models.IntegerField(null=True)

    def __str__(self):
        return str(self.code)


class StatusNumber(models.Model):
    code_number = models.ForeignKey(CodeNumber, on_delete=models.CASCADE, null=True)
    number = models.IntegerField(null=True)
    STATUS_CHOICES = (
        ('Золото+', 'gold'),
        ('Платина', 'platinum'),
        ('VIP', 'vip'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return f'({self.code_number}) {self.number}'


class TariffInternetM2M(models.Model):
    """Тарифы для M2M-оборудования"""
    title = models.CharField(max_length=46, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)
    gigabytes = RichTextField(null=True)
    price = models.IntegerField(null=True)


class NextTariffInternetM2M(models.Model):
    """Продолжения Тарифа InternetM2M"""
    internet_m2m = models.ForeignKey(TariffInternetM2M, on_delete=models.CASCADE, null=True)
    COMMUNICATION_CHOICES = (
        ('Звонки', 'call'),
        ('SMS', 'sms'),
    )
    communication_type = models.CharField(max_length=100, choices=COMMUNICATION_CHOICES, null=True)
    rich_internet2m2 = RichTextField(null=True)


class RelatedServices(models.Model):
    """Связанные услуги"""
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)


class AdvantagesM2M(models.Model):
    """Преимущества"""
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(null=True)
    logo = models.ImageField(null=True)


class Package(models.Model):
    """Интернет пакеты 15,25"""
    title = models.CharField(max_length=55)
    price = models.IntegerField()
    image = models.ImageField()
    gigabytes = models.IntegerField()
    it_work = models.CharField(max_length=45)
    plug_ussd = models.CharField(max_length=15)
    unplug_ussd = models.CharField(max_length=15)
    check_ussd = models.CharField(max_length=15)


class Questions(models.Model):
    """Часто Задаваемые Вопросы"""
    questions = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)

    def __str__(self):
        return self.questions
