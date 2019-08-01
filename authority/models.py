from django.db import models

# Create your models here.
class Authority(models.Model):
    title = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d')
    email = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 50)
    description = models.TextField(blank = True)


    def __str__(self):
        return self.title