from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    """
    Represents category of items on menu like Appetizers, Main Course, Desserts etc.
    Name field is unique 
    """
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name
