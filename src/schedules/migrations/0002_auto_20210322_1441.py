# Generated by Django 2.2.13 on 2021-03-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='eventDate',
            field=models.DateTimeField(),
        ),
    ]
