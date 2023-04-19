# Generated by Django 3.1.1 on 2023-04-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('Productid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Brandname', models.CharField(max_length=100)),
                ('Modelname', models.CharField(max_length=80)),
                ('Os', models.CharField(max_length=100)),
                ('Colour', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
