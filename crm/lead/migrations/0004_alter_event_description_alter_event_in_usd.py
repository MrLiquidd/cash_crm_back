# Generated by Django 5.0.6 on 2024-06-18 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0003_alter_event_in_usd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='in_usd',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]