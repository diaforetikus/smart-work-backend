# Generated by Django 4.1.5 on 2023-02-01 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0003_rename_user_job_executor_job_completed_at_job_owner_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jobcategory",
            old_name="title",
            new_name="name",
        ),
    ]