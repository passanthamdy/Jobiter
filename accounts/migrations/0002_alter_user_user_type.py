# Generated by Django 4.0.5 on 2022-07-07 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('EMPLOYEE', 'Employee'), ('COMPANY', 'Company')], default='EMPLOYEE', max_length=50),
        ),
    ]
