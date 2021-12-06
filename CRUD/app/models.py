from django.db import models


# Create your models here.
class User(models.Model):
    Email=models.EmailField()
    Username=models.CharField(max_length=1000)
    def __str__(self):
        return  self.id



    

