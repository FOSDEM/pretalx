# Generated by Django 2.0.1 on 2018-01-26 15:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0017_auto_20180115_1743"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="submissiontype",
            name="max_duration",
        ),
    ]
