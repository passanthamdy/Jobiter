# Generated by Django 4.0.5 on 2022-07-23 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_appliedemployees_created_at_job_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedemployees',
            name='cover_letter',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='appliedemployees',
            name='notice_period',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
