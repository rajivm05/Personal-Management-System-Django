# Generated by Django 2.2.13 on 2021-03-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0005_auto_20210324_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedules',
            name='eventEnd',
            field=models.DateTimeField(help_text="<br><p ><ul><li id='warningText'>The end time must be later than the start time.</ul></li><p>"),
        ),
    ]
