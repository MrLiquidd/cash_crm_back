# Generated by Django 4.2.13 on 2024-06-20 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('Регистрация', 'Регистрация'), ('Звонок', 'Звонок'), ('Консультация', 'Консультация'), ('Лекция', 'Лекция'), ('Практика', 'Практика'), ('Стажировка', 'Стажировка'), ('Конец стажировки', 'Конец стажировки'), ('Мастер класс', 'Мастер класс'), ('Вопрос о счете', 'Вопрос о счете'), ('Школа трейда', 'Школа трейда'), ('Последняя практика', 'Последняя практика'), ('Открытие счета', 'Открытие счета'), ('Пополнение счета', 'Пополнение счета'), ('Встреча', 'Встреча')], max_length=50, verbose_name='Тип события')),
                ('data', models.DateTimeField()),
                ('status', models.CharField(choices=[('Запланировано', 'Запланировано'), ('Обработано', 'Обработано'), ('Выполнено', 'Выполнено'), ('Просрочено', 'Просрочено')], max_length=50, verbose_name='Статус')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('in_usd', models.CharField(blank=True, max_length=50, null=True, verbose_name='В долларах')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_client', to='leads.lead')),
                ('reflective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reflective_event', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]