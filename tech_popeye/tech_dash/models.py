from django.db import models

# Create your models here.


class CarouselItem(models.Model):
    image = models.ImageField(upload_to='static/img/carousel_images')
    caption = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.caption

class Feature(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    from django.db import models

class Service(models.Model):
    image = models.ImageField(upload_to='static/img/service_images')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title



class ContactMessage(models.Model):
    name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(blank=False)
    subject = models.CharField(max_length=255,blank=False)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.name
