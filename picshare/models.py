from django.db import models

# Create your models here.
class Images(models.Model):
    # image = models.ImageField(upload_to = 'images/', default = 'image.jpeg')
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey('Location')
    category = models.ForeignKey('Category')


class Category(models.Model):
    category_name = models.CharField(max_length = 30)


class Location(models.Model):
    location_name = models.CharField(max_length = 30)