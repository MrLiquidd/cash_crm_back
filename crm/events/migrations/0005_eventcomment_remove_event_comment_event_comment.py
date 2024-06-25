# Generated by Django 4.2.13 on 2024-06-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_office'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='comment',
        ),
        migrations.AddField(
            model_name='event',
            name='comment',
            field=models.ManyToManyField(to='events.eventcomment', verbose_name='Комментарий'),
        ),
    ]
