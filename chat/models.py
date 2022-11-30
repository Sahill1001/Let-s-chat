from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.name 

class Message(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    msg = models.CharField(max_length=5000)
    time = models.CharField(max_length=50)
    def __str__(self):
        return self.msg 
