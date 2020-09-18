from django.db import models

# Create your models here.

class medicine(models.Model):
    medicine_id = models.AutoField
    medicine_name = models.CharField(max_length=50,default=None)
    medicine_drug_content = models.CharField(max_length=500,default=None)

    def __str__(self):
        return self.medicine_name


class patient(models.Model):
    patient_id = models.AutoField
    patient_name = models.CharField(max_length=50,default=None)
    patient_DOB = models.DateField(default=None)
    patient_address = models.CharField(max_length=500,default=None)
    patient_current_medicine = models.CharField(max_length=500,default=None)
    medicines = models.ManyToManyField(medicine)


    #to display good name outside the database
    def __str__(self):
        return self.patient_name


class medical(models.Model):
    medical_id = models.AutoField
    medical_name = models.CharField(max_length=500,default=None)
    medical_address = models.CharField(max_length=500,default=None)
    medical_timing = models.CharField(max_length=500,default=None)
    medical_phone = models.CharField(max_length=500,default=None)
    medicines = models.ManyToManyField(medicine)
    def __str__(self):
        return self.medical_name



