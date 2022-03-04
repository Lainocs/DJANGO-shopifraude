from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.title
    
# Create your models here.
