# Generated by Django 4.0.5 on 2022-07-17 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('job_title', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(default=None, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_company_id', to=settings.AUTH_USER_MODEL, verbose_name='Company')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_employee_id', to=settings.AUTH_USER_MODEL, verbose_name='Reviewer')),
            ],
            options={
                'verbose_name': 'Salary',
            },
        ),
    ]
