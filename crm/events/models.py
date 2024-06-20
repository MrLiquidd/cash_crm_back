from django.db import models

from accounts.models import User
from leads.models import Lead


class Event(models.Model):
    registration = 'Регистрация'
    call = 'Звонок'
    consultation = 'Консультация'
    lesson = 'Лекция'
    practice = 'Практика'
    internship = 'Стажировка'
    end_internship = 'Конец стажировки'
    master_class = 'Мастер класс'
    question_check = 'Вопрос о счете'
    school_of_trade = 'Школа трейда'
    last_practice = 'Последняя практика'
    open_check = 'Открытие счета'
    add_check = 'Пополнение счета'
    event = 'Встреча'

    planned = 'Запланировано'
    processed = 'Обработано'
    complete = 'Выполнено'
    failed = 'Просрочено'

    CHOICES_TYPE = (
        (registration, 'Регистрация'),
        (call, 'Звонок'),
        (consultation, 'Консультация'),
        (lesson, 'Лекция'),
        (practice, 'Практика'),
        (internship, 'Стажировка'),
        (end_internship, 'Конец стажировки'),
        (master_class, 'Мастер класс'),
        (question_check, 'Вопрос о счете'),
        (school_of_trade, 'Школа трейда'),
        (last_practice, 'Последняя практика'),
        (open_check, 'Открытие счета'),
        (add_check, 'Пополнение счета'),
        (event, 'Встреча'),
    )

    CHOICES_STATUS = (
        (planned, 'Запланировано'),
        (processed, 'Обработано'),
        (complete, 'Выполнено'),
        (failed, 'Просрочено')
    )

    event_type = models.CharField(max_length=50, choices=CHOICES_TYPE, verbose_name='Тип события')
    data = models.DateTimeField()
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, verbose_name='Статус')
    reflective = models.ForeignKey(
        User, related_name='reflective_event', on_delete=models.CASCADE
    )
    client = models.ForeignKey(Lead, related_name='event_client', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    comment = models.TextField(null=True, blank=True, verbose_name='Комментарий')
    in_usd = models.CharField(max_length=50, null=True, blank=True, verbose_name='В долларах')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')
    is_active = models.BooleanField(default=True, verbose_name='Активность')

    def __str__(self):
        return f'{self.client} + {self.reflective}: {self.event_type}'
