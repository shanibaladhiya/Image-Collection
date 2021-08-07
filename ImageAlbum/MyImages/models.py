from django.db import models

class imagesUpload(models.Model):
    category = models.CharField(max_length=50, blank=True ,default='Nature' ,choices=[('Nature','Nature'),('Food','Food')])
    photo = models.ImageField(upload_to='galleryImages/', height_field=None, width_field=None, max_length=None, blank=True)
    imagename = models.CharField(max_length=50, blank=True)

# class Categories(models.Model):
#     CategoryName = models.CharField(max_length=50, blank=True)
#     CategoryImage = models.ImageField(upload_to='categoryPoster/', height_field=None, width_field=None, max_length=None, blank=True)
    
class Contactus(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=10, blank=True)
    msg = models.TextField(max_length=50, blank=True)