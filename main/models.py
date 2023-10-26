
from datetime import datetime
from django.db import models

# Create your models here.



# class Skill(models.Model):
#     name = models.CharField(max_length=300, blank=True)
#     percent = models.IntegerField(max_length=3, blank=True)
#     comment = models.TextField(blank=True,null=True)
#
#     def __str__(self):
#         return f'{self.name} {self.percent}'



class Case(models.Model):
    title = models.CharField(max_length=300, blank=True)
    category = models.CharField(max_length=300, blank=True)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to='upload', blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.title}'


# class Resume(models.Model):
#     title = models.CharField(max_length=300, blank=True)
#     subtitle = models.CharField(max_length=300, blank=True)
#     date = models.TextField(blank=True,null=True)
#     status = models.IntegerField(blank=True, default=0)
#
#     def __str__(self):
#         return f'{self.title} {self.subtitle}'



class Feedback(models.Model):
    name = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    comment = models.TextField(blank=True,null=True)

    def __str__(self):
        return f'{self.name} {self.phone}'


class Blog(models.Model):
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(max_length=500, blank=True)
    date = models.DateField(blank=True,default=datetime.now())
    photo = models.ImageField(upload_to='upload', blank=True)
    link = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f'{self.title}'