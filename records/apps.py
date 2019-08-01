from django.db import models
from datetime import datetime

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length = 100)
    roll = models.CharField(max_length = 50)
    batch = models.CharField(max_length = 100)
    department = models.CharField(max_length = 100)
    Student_Contact = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    father = models.CharField(max_length = 100)
    Father_Contact = models.CharField(max_length = 50)
    mother = models.CharField(max_length = 100)
    Mother_Contact = models.CharField(max_length = 50)
    religion = models.CharField(max_length = 50)
    nationality = models.CharField(max_length = 50)
    blood = models.CharField(max_length = 20)
    street = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    district = models.CharField(max_length = 50)
    zip_code = models.CharField(max_length = 50)
    college = models.CharField(max_length = 100)
    HSC_Result = models.CharField(max_length = 5)
    HSC_Group = models.CharField(max_length = 50)
    HSC_Board = models.CharField(max_length = 50)
    HSC_Year = models.CharField(max_length = 50)
    school = models.CharField(max_length = 50)
    SSC_Result = models.CharField(max_length = 5)
    SSC_Group = models.CharField(max_length = 50)
    SSC_Board = models.CharField(max_length = 30)
    SSC_Year = models.CharField(max_length = 20)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    is_published = models.BooleanField(default = True)
    list_date = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return self.name