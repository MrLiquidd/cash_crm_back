import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from leads.managers import CustomUserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True, verbose_name='Изображение профиля')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    term_work = models.DateTimeField(auto_now_add=True)
    passport = models.CharField(max_length=55, verbose_name='Паспорт', null=True, blank=True)
    hire_data = models.DateTimeField(auto_now_add=True)
    office = models.CharField(max_length=255, verbose_name='Офис', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='Номер телефона', null=True, blank=True)
    surname = models.CharField(max_length=255, verbose_name='Фамилия', null=True, blank=True)
    last_name = models.CharField(max_length=255, verbose_name='Отчество', null=True, blank=True)
    job_title = models.CharField(max_length=255, default='Стажер', verbose_name='Должность', null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.surname}".strip()
