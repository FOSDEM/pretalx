# Generated by Django 2.0.1 on 2018-01-15 23:43

from django.db import migrations


def fix_speaker_answers(apps, schema_editor):
    Question = apps.get_model("submission", "Question")
    for question in Question.objects.filter(target="speaker"):
        for answer in question.answers.filter(person__isnull=True):
            try:
                answer.person = answer.submission.speakers.first()
                answer.submission = None
                answer.save()
            except Exception:
                pass


class Migration(migrations.Migration):
    dependencies = [
        ("submission", "0016_auto_20171114_1251"),
    ]

    operations = [migrations.RunPython(fix_speaker_answers, migrations.RunPython.noop)]
