from django.db import models


class Doctors(models.Model):
    name = models.CharField(max_length=100)
    specialize = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name;
