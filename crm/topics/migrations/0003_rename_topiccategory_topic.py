# Generated by Django 4.2.13 on 2024-06-25 09:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0002_remove_topiccategory_reflective_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TopicCategory',
            new_name='Topic',
        ),
    ]
