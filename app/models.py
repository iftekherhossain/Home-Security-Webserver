from django.db import models

# Create your models here.

class My_Model(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    
    
    def __str__(self):
        return self.name