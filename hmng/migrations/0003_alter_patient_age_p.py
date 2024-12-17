# Generated by Django 5.1.1 on 2024-12-11 06:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmng', '0002_alter_patient_age_p_alter_patient_gender_p'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age_p',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(120)]),
        ),
    ]
