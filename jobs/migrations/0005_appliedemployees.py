# Generated by Django 4.0.5 on 2022-07-13 00:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_company_options_alter_employee_options_and_more'),
        ('jobs', '0004_remove_job_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppliedEmployees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.FileField(blank=True, null=True, upload_to='user_cvs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])])),
                ('notice_period', models.IntegerField()),
                ('years_of_exp', models.IntegerField()),
                ('cover_letter', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.employee', verbose_name='Employee')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job', verbose_name='Job')),
            ],
        ),
    ]
