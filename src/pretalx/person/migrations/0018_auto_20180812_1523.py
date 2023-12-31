# Generated by Django 2.0.8 on 2018-08-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("person", "0017_auto_20180530_1434"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="locale",
            field=models.CharField(default="en", max_length=32),
        ),
        migrations.AlterField(
            model_name="user",
            name="nick",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
