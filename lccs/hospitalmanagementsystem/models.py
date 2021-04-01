from django.db import models
from django.forms import ModelForm

import uuid

# Create your models here.
class doctor(models.Model):
  UID = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
  name = models.CharField(max_length=50)
  position = models.CharField(max_length=100)
  speciality = models.CharField(max_length=100)
  joinDate = models.DateField()
  nationality = models.CharField(max_length=100)
  
  def __str__(self):
        return 'Doctor: {}'.format(self.name)
  
class patient(models.Model):
  UID = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
  name = models.CharField(max_length=100)
  dob = models.DateField(max_length=20)
  dateAdmitted =  models.DateField()
  doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
  discharged = models.BooleanField()
  bloodType = models.CharField(max_length=10)
  
  def __str__(self):
        return 'Patient: {}'.format(self.name)
  
class room(models.Model):
  UID = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
  roomNumber = models.IntegerField()
  occupied = models.BooleanField(null=True, blank=True)
  patientID = models.ForeignKey(patient, on_delete=models.CASCADE, blank=True, null=False)
  floor = models.IntegerField()
  
  def __str__(self):
        return 'Room: {}'.format(self.roomNumber)