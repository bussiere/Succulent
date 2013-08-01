from django.db import models

# Create your models here.

class Bookmark(models.Model):
    url = models.ForeignKey('Url')
    description = models.ForeignKey('Description')
    image = models.ForeignKey('Image')
    tag = models.ManyToManyField("Tag")
    title = models.ForeignKey('Title')
    Private = models.ForeignKey('Private')
    

class Private(models.Model):
    Private = models.BooleanField(default='False')

class Title(models.Model):
    title = models.CharField(max_length=5024)    
    
class Url(models.Model):
    url = models.CharField(max_length=5024)



class Description(models.Model):
    description = models.CharField(max_length=1024)

    
    
class Image(models.Model):
    image = models.ImageField(upload_to="image")
    
class Tag(models.Model):
    tag = models.CharField(max_length=1024)