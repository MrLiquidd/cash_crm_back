# Generated by Django 4.2.13 on 2024-06-25 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
        ('accounts', '0002_remove_user_office'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='office',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_office', to='office.office'),
            preserve_default=False,
        ),
    ]
