# Generated by Django 2.1.5 on 2019-02-22 22:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mail", "0003_auto_20171001_1358"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailtemplate",
            name="reply_to",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
