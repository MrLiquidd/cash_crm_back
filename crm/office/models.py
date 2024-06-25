from django.db import models


class Office(models.Model):
    office = models.CharField(max_length=50, verbose_name='Название офиса')
    city = models.CharField(max_length=50, verbose_name='Город')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    region = models.CharField(max_length=255, verbose_name='Регион')
    groupOffice = models.CharField(max_length=255, verbose_name='Группа Офисов')
    payday = models.IntegerField(verbose_name='День выплат')

    def __str__(self):
        return self.office
