# Generated by Django 4.2.13 on 2024-06-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_event_type_alter_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('Регистрация', 'Регистрация'), ('Звонок', 'Звонок'), ('Консультация', 'Консультация'), ('Лекция', 'Лекция'), ('Практика', 'Практика'), ('Стажировка', 'Стажировка'), ('Конец стажировки', 'Конец стажировки'), ('Мастер класс', 'Мастер класс'), ('Вопрос о счете', 'Вопрос о счете'), ('Школа трейда', 'Школа трейда'), ('Последняя практика', 'Последняя практика'), ('Открытие счета', 'Открытие счета'), ('Пополнение счета', 'Пополнение счета'), ('Встреча', 'Встреча')], max_length=50, verbose_name='Тип события'),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Запланировано', 'Запланировано'), ('Обработано', 'Обработано'), ('Выполнено', 'Выполнено'), ('Просрочено', 'Просрочено')], max_length=50, verbose_name='Статус'),
        ),
    ]
