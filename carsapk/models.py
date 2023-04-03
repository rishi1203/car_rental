from django.db import models

# Create your models here.
class Cars_Dest(models.Model):
    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    discription = models.TextField()
    offer = models.BooleanField(default=False)
           
# class Cars_Fleet(models.Model):
#     img = models.ImageField(upload_to='images')
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     discription = models.TextField()
#     offer = models.BooleanField(default=False)

# class Cars_Offers(models.Model):
#     img = models.ImageField(upload_to='images')
#     name = models.CharField(max_length=100)
#     price = models.IntegerField()
#     discription = models.TextField()
#     offer = models.BooleanField(default=False)