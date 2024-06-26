from django.db import models
from accounts.models import User
from office.models import Office


class Lead(models.Model):
    VIP = 'vip'
    FUCK_OFF = 'fuck_off'
    ALL_AGREE = 'all_agree'
    POTENTIAL = 'potential'
    BND = 'bnd'
    BIRSHA_WORK = 'birsha_work'
    FSSP = 'fssp'
    BANKRUPT = 'bankrupt'

    CHOICES_STATUS = (
        (VIP, 'vip'),
        (FUCK_OFF, 'FUCK OFF'),
        (ALL_AGREE, 'На все согласен'),
        (POTENTIAL, 'Потенциальный'),
        (BND, 'БнД'),
        (BIRSHA_WORK, 'Биржа труда'),
        (FSSP, 'ФССП'),
        (BANKRUPT, 'Банкрот'),
    )

    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    gender = models.CharField(max_length=10)
    office = models.ForeignKey(Office, related_name='lead_office', on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, null=True, blank=True, verbose_name='Статус')
    manager = models.ForeignKey(
        User, related_name='leads', on_delete=models.CASCADE, verbose_name='Менеджер'
    )
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')


    def __str__(self):
        return self.name
