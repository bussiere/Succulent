from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    origin = models.CharField(max_length=15,null=True, blank=True)
    url = models.CharField(max_length=5024,null=True, blank=True)

class Bookmark(models.Model):
    user = models.ManyToManyField(User)
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    url = models.ForeignKey('Url',null=True, blank=True)
    description = models.ForeignKey('Description',null=True, blank=True)
    image = models.ForeignKey('Image',null=True, blank=True)
    tag = models.ManyToManyField("Tag",null=True, blank=True)
    title = models.ForeignKey('Title',null=True, blank=True)
    private = models.ForeignKey('Private',null=True, blank=True)
    def __unicode__(self):
        return ("%s %s"%(str(self.url),str(self.description)))
    class Meta:
        ordering = ['Date']
    

class Private(models.Model):
    private = models.BooleanField(default='False')
    def __unicode__(self):
        return str(self.private)

class Title(models.Model):
    title = models.CharField(max_length=5024,null=True, blank=True)
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return str(self.title)
    
    
class Url(models.Model):
    url = models.CharField(max_length=5024,null=True, blank=True)
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return str(self.url)




class Description(models.Model):
    description = models.CharField(max_length=1024,null=True, blank=True)
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return str(self.description)


    
    
class Image(models.Model):
    image = models.ImageField(upload_to="image",null=True, blank=True)
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    def __unicode__(self):
        return str(self.image)

    
class Tag(models.Model):
    user = models.ManyToManyField(User)
    Date =  models.DateTimeField(auto_now_add=True, blank=True)
    tag = models.CharField(max_length=1024,null=True, blank=True)
    def save(self):
        self.tag = self.tag.replace("+","")
        self.save()
    def __unicode__(self):
        return str(self.tag)
    class Meta:
        ordering = ['tag']
