from django.db import models

# Create your models here.

class Bookmark(models.Model):
    url = models.ForeignKey('Url',null=True, blank=True)
    description = models.ForeignKey('Description',null=True, blank=True)
    image = models.ForeignKey('Image',null=True, blank=True)
    tag = models.ManyToManyField("Tag",null=True, blank=True)
    title = models.ForeignKey('Title',null=True, blank=True)
    private = models.ForeignKey('Private',null=True, blank=True)
    

class Private(models.Model):
    private = models.BooleanField(default='False')

class Title(models.Model):
    title = models.CharField(max_length=5024,null=True, blank=True)    
    
class Url(models.Model):
    url = models.CharField(max_length=5024,null=True, blank=True)



class Description(models.Model):
    description = models.CharField(max_length=1024,null=True, blank=True)

    
    
class Image(models.Model):
    image = models.ImageField(upload_to="image",null=True, blank=True)
    
class Tag(models.Model):
    tag = models.CharField(max_length=1024,null=True, blank=True)