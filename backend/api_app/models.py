from django.db import models

# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name
    
