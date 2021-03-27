# Generated by Django 2.2.13 on 2021-03-24 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('money', models.FloatField()),
                ('billDescription', models.CharField(max_length=10000)),
                ('billType', models.CharField(choices=[('Monthly Payments', 'Monthly Paymentsc'), ('Personal', 'Personal'), ('Domestic', 'Domestic'), ('Travels', 'Travels'), ('Food', 'Food'), ('Entertainment', 'Entertainment')], default='Monthly Payments', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]