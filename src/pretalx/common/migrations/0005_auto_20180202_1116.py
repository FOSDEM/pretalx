# Generated by Django 2.0.1 on 2018-02-02 17:16

from django.db import migrations


def fix_log_action(apps, schema_editor):
    ActivityLog = apps.get_model("common", "ActivityLog")
    ActivityLog.objects.all().filter(action_type="update").update(
        action_type="pretalx.submission.update"
    )


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0004_auto_20170526_0437"),
    ]

    operations = [migrations.RunPython(fix_log_action, migrations.RunPython.noop)]
