# Generated by Django 4.1.7 on 2023-06-27 23:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("notice", "0002_notice_delete_article"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notice",
            name="student_id",
        ),
    ]
