# Generated by Django 4.2 on 2023-04-30 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mapelementmodel",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="maplayermodel",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
