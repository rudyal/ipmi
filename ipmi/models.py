from django.db import models
# Create your models here.
class wouldyourather(models.Model):
    question = models.CharField(max_length=100)
    meta1 = models.CharField(max_length=100)
    meta2 = models.CharField(max_length=100)
    answer1 = models.BooleanField()
    answer2 = models.BooleanField()

    def __str__(self):              # __unicode__ on Python 2
        return self.question

class ipmi(models.Model):
    serv_name = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    cpu_temp = models.CharField(max_length=100)
    cpu_temp2 = models.CharField(max_length=100)
    fan_speed = models.CharField(max_length=100)
    air = models.CharField(max_length=100)
    knox = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    meta1 = models.CharField(max_length=100)
    meta2 = models.CharField(max_length=100)
    meta3 = models.CharField(max_length=100)
    meta4 = models.CharField(max_length=100)
    meta5 = models.CharField(max_length=100)

    def __str__(self):              # __unicode__ on Python 2
        return self.serv_name