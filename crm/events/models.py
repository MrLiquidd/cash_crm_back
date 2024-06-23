from django.db import models

from accounts.models import User
from leads.models import Lead


class Event(models.Model):
    REGISTRATION = 'Регистрация'
    CALL = 'Звонок'
    CONSULTATION = 'Консультация'
    LESSON = 'Лекция'
    PRACTICE = 'Практика'
    INTERNSHIP = 'Стажировка'
    END_INTERNSHIP = 'Конец стажировки'
    MASTER_CLASS = 'Мастер класс'
    QUESTION_CHECK = 'Вопрос о счете'
    SCHOOL_OF_TRADE = 'Школа трейда'
    LAST_PRACTICE = 'Последняя практика'
    OPEN_CHECK = 'Открытие счета'
    ADD_CHECK = 'Пополнение счета'
    EVENT = 'Встреча'

    PLANNED = 'Запланировано'
    PROCESSED = 'Обработано'
    COMPLETE = 'Выполнено'
    FAILED = 'Просрочено'

    CHOICES_TYPE = (
        (REGISTRATION, 'Регистрация'),
        (CALL, 'Звонок'),
        (CONSULTATION, 'Консультация'),
        (LESSON, 'Лекция'),
        (PRACTICE, 'Практика'),
        (INTERNSHIP, 'Стажировка'),
        (END_INTERNSHIP, 'Конец стажировки'),
        (MASTER_CLASS, 'Мастер класс'),
        (QUESTION_CHECK, 'Вопрос о счете'),
        (SCHOOL_OF_TRADE, 'Школа трейда'),
        (LAST_PRACTICE, 'Последняя практика'),
        (OPEN_CHECK, 'Открытие счета'),
        (ADD_CHECK, 'Пополнение счета'),
        (EVENT, 'Встреча'),
    )

    CHOICES_STATUS = (
        (PLANNED, 'Запланировано'),
        (PROCESSED, 'Обработано'),
        (COMPLETE, 'Выполнено'),
        (FAILED, 'Просрочено')
    )

    event_type = models.CharField(max_length=50, choices=CHOICES_TYPE, verbose_name='Тип события')
    data = models.DateTimeField()
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, verbose_name='Статус')
    reflective = models.ForeignKey(
        User, related_name='reflective_event', on_delete=models.CASCADE, verbose_name='Ответственный'
    )
    client = models.ForeignKey(Lead, related_name='event_client', on_delete=models.CASCADE, verbose_name='Клиент')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    in_usd = models.CharField(max_length=50, null=True, blank=True, verbose_name='В долларах')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    def __str__(self):
        return f'{self.client} + {self.reflective}: {self.event_type}'
