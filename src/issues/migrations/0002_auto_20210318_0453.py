# Generated by Django 2.2.13 on 2021-03-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issues',
            name='lastProgress',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='issues',
            name='startDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
