# Generated by Django 2.2.13 on 2021-03-22 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_auto_20210322_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='eventDuration',
            field=models.DurationField(),
        ),
    ]
