# Generated by Django 4.1.5 on 2023-02-02 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("jobs", "0006_alter_job_description_alter_job_executor_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="proposal",
            name="job",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="jobs.job"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="proposal",
            name="user",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
