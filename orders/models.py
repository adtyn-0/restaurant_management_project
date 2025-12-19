from django.db import models

# Create your models here.
class OrderStatus(models.Model):
    """
    Represents the state of order in workflow with states like: Pending, Completed or Cancelled etc. 
    """
    order_status = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.order_status
