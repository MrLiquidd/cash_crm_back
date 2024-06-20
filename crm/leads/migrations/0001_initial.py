# Generated by Django 4.2.13 on 2024-06-20 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('office', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('status', models.CharField(choices=[('vip', 'vip'), ('FUCK OFF', 'FUCK OFF'), ('На все согласен', 'На все согласен'), ('Потенциальный', 'Потенциальный'), ('БнД', 'БнД'), ('Биржа труда', 'Биржа труда'), ('ФССП', 'ФССП'), ('Банкрот', 'Банкрот')], max_length=50, null=True, verbose_name='Статус')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads', to=settings.AUTH_USER_MODEL, verbose_name='Менеджер')),
            ],
        ),
    ]