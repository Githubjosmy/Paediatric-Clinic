# Generated by Django 4.1.7 on 2023-04-17 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accountsapp', '0004_alter_patient_data_blood_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_data',
            name='DOB',
            field=models.DateField(auto_now_add=True),
        ),
    ]
