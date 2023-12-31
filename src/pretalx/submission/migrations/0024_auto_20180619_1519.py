# Generated by Django 2.0.3 on 2018-06-19 20:19

from django.db import migrations


def rebuild_review_codes(apps, schema_editor):
    from pretalx.submission.models.submission import generate_invite_code

    Submission = apps.get_model("submission", "Submission")

    for pk in Submission.objects.all().values_list("pk", flat=True):
        submission = Submission.objects.get(pk=pk)
        submission.review_code = generate_invite_code()
        submission.save()


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0023_submission_is_featured"),
    ]

    operations = [
        migrations.RunPython(rebuild_review_codes, migrations.RunPython.noop),
    ]
