# Generated by Django 2.1.5 on 2019-02-23 21:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0031_auto_20190223_0730"),
    ]

    operations = [
        migrations.AddField(
            model_name="question",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
    ]
