from django.db import models
class Patient_data(models.Model):
    blood_choice = (
        ('O +ve' ,'O +ve'),
        ('O -ve','O -ve'),
        ('A +ve','A +ve'),
        ('B +ve','B +ve'),
        ('A -ve','A -ve'),
        ('AB +ve','AB +ve'),
    )

    doctor_name = models.CharField(max_length=100)
    spec = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Phone_no = models.CharField(max_length=100)
    DOB = models.DateField(auto_now_add=False)
    BLOOD_TYPE = models.CharField(choices=blood_choice,max_length=100)
    Address = models.TextField(max_length=100)
    Gender = models.CharField(max_length=100)
    Polio = models.CharField(max_length=100, default='Polio-IPV Vaccine', editable=False)
    Prev_dose = models.CharField(max_length=100)
    Appt_date = models.DateField(auto_now_add=False)
    Appt_time = models.TimeField(auto_now_add=False)


    def __str__(self):
        return self.first_name + self.Last_name;
