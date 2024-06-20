from django.db import models
from accounts.models import User


class Lead(models.Model):
    VIP = 'vip'
    FUCK_OFF = 'FUCK OFF'
    ALL_AGREE = 'На все согласен'
    POTENTIAL = 'Потенциальный'
    BnD = 'БнД'
    BIRSHA_WORK = 'Биржа труда'
    FSSP = 'ФССП'
    BANKRUPT = 'Банкрот'

    CHOICES_STATUS = (
        (VIP, 'vip'),
        (FUCK_OFF, 'FUCK OFF'),
        (ALL_AGREE, 'На все согласен'),
        (POTENTIAL, 'Потенциальный'),
        (BnD, 'БнД'),
        (BIRSHA_WORK, 'Биржа труда'),
        (FSSP, 'ФССП'),
        (BANKRUPT, 'Банкрот'),
    )

    name = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, null=True, verbose_name='Статус')
    manager = models.ForeignKey(
        User, related_name='leads', on_delete=models.CASCADE, verbose_name='Менеджер'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')

    def __str__(self):
        return self.name
