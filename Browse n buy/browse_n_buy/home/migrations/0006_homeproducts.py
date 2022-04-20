# Generated by Django 3.2.7 on 2021-09-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_product_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homeproducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=15)),
                ('product_desc', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='home/home_prod')),
            ],
        ),
    ]
