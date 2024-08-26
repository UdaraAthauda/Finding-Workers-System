from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class WorkerArea(models.Model):
    areaName = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return self.areaName


class WorkerDetails(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Worker_image = models.ImageField(upload_to='images/', blank=True, null=True, default='images/propic.jpeg')
    Contact_number = models.IntegerField()
    Location = models.CharField(max_length=100)
    Working_areas = models.ManyToManyField(WorkerArea, related_name='areas')
    Experience = models.CharField(max_length=50)
    Description = models.TextField()
    Reg_date = models.DateField(auto_now_add=True)
    Accept = models.BooleanField(default=False)

    def __str__(self):
        return self.First_name + " " + self.Last_name
