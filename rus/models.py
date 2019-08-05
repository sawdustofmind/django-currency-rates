from django.db import models
    
class Rate(models.Model):
    currency = models.CharField(max_length=30, unique=True)
    rate = models.FloatField()
    
    def __str__(self):
        return self.currency