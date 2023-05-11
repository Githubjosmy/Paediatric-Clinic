# Generated by Django 4.1.7 on 2023-03-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accountsapp', '0003_patient_data_blood_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_data',
            name='BLOOD_TYPE',
            field=models.CharField(choices=[('O +ve', 'O +ve'), ('O -ve', 'O -ve'), ('A +ve', 'A +ve'), ('B +ve', 'B +ve'), ('A -ve', 'A -ve'), ('AB +ve', 'AB +ve')], max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='Polio',
            field=models.CharField(default='Polio-IPV Vaccine', editable=False, max_length=100),
        ),
    ]