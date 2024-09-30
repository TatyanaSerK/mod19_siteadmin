from django.db import models

# Create your models here.
class Test(models.Model):
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    numb = models.IntegerField()
    text = models.TextField()