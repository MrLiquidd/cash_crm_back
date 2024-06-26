# Generated by Django 4.2.13 on 2024-06-25 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
        ('events', '0003_alter_event_event_type_alter_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='office',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='event_office', to='office.office'),
            preserve_default=False,
        ),
    ]
