# Generated by Django 3.2.7 on 2021-09-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_customer_subscriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]