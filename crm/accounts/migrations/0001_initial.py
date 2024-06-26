# Generated by Django 4.2.13 on 2024-06-20 13:54

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import leads.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Изображение профиля')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('term_work', models.DateTimeField(auto_now_add=True)),
                ('passport', models.CharField(blank=True, max_length=55, null=True, verbose_name='Паспорт')),
                ('hire_data', models.DateTimeField(auto_now_add=True)),
                ('office', models.CharField(blank=True, max_length=255, null=True, verbose_name='Офис')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер телефона')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Фамилия')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('job_title', models.CharField(blank=True, default='Стажер', max_length=255, null=True, verbose_name='Должность')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', leads.managers.CustomUserManager()),
            ],
        ),
    ]
