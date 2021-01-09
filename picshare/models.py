from django.db import models

# Create your models here.
class Images(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()


class Category(models.Model):
    category_name = models.CharField(max_length = 30)


class Location(models.Model):
    location_name = models.CharField(max_length = 30)