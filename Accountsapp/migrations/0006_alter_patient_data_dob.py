# Generated by Django 4.1.7 on 2023-04-17 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accountsapp', '0005_alter_patient_data_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_data',
            name='DOB',
            field=models.DateField(),
        ),
    ]