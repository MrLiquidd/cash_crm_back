from django.db import models

from accounts.models import User


# Create your models here.
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

    theme = models.CharField(max_length=255, verbose_name='Тема')
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, verbose_name='Статус')
    reflective = models.ForeignKey(User, related_name='reflective_topic', on_delete=models.CASCADE)
    personal_access = models.ForeignKey(User, related_name='personal_topic', on_delete=models.CASCADE)
    open_topic = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время открытия топика')
    deadline = models.DateTimeField(verbose_name='Крайний срок', blank=True, null=True)
    author = models.ForeignKey(
        User, related_name='author_topic', on_delete=models.CASCADE, verbose_name='Автор'
    )

    def __str__(self):
        return self.theme
