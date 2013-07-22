from django.db import models

# Create your models here.

class Bookmark(models.Model):
    url = models.ForeignKey('Url')
    description = models.ForeignKey('Description')
    image = models.ForeignKey('Image')
    tag = models.ManyToManyField("Tag")
    
    
    
    
class Url(models.Model):
    url = models.CharField(max_length=1024)



class Description(models.Model):
    description = models.CharField(max_length=1024)

    
    
class Image(models.Model):
    image = models.ImageField(upload_to="image")
    
class Tag(models.Model):
    tag = models.CharField(max_length=1024)