import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractBaseUser
from django.utils import timezone


class CustomUserManager(UserManager):
    def _create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    email = models.EmailField(unique=True)

    last_login = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email


class UserInfo(models.Model):
    user = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255, default='Стажер')
    surname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    term_work = models.DateTimeField(auto_now_add=True)
    passport = models.CharField(max_length=55)
    hire_data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def full_name(self):
        return f"{self.name} {self.surname}".strip()


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
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, null=True)
    manager = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


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

    event_type = models.CharField(max_length=50, choices=CHOICES_TYPE)
    data = models.DateTimeField()
    status = models.CharField(max_length=50, choices=CHOICES_STATUS)
    reflective = models.ForeignKey(User, related_name='reflective_event', on_delete=models.CASCADE)
    client = models.ForeignKey(Lead, related_name='event_client', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    in_usd = models.CharField(max_length=50, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.client} + {self.reflective}: {self.event_type}'


class TopicCategory(models.Model):
    not_ready = 'Не начато'
    im_work = 'В работе'
    attention = 'Требует внимания'
    discussion = 'Обсуждение'
    complete = 'Выполнено'
    failed = 'Просрочено'

    CHOICES_STATUS = (
        (not_ready, 'Не начато'),
        (im_work, 'В работе'),
        (attention, 'Требует внимания'),
        (discussion, 'Обсуждение'),
        (complete, 'Выполнено'),
        (failed, 'Просрочено')
    )

    theme = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=CHOICES_STATUS)
    reflective = models.ForeignKey(User, related_name='reflective_topic', on_delete=models.CASCADE)
    personal_access = models.ForeignKey(User, related_name='personal_topic', on_delete=models.CASCADE)
    open_topic = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    author = models.ForeignKey(User, related_name='author_topic', on_delete=models.CASCADE)

    def __str__(self):
        return self.theme
