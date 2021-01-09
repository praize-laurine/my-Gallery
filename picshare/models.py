from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to = 'images/', default = 'image.jpeg')
    name = models.CharField(max_length = 30)
    description = models.TextField()
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, default = '', null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains = search_term)
        return images  

    def update_image(self, Name=None, category=None):
        self.name = Name if Name else self.Name
        self.category = category if category else self.category 
        self.save()    

    def __str__(self):
        return self.name
     



class Category(models.Model):
    category_name = models.CharField(max_length = 30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.category_name


class Location(models.Model):
    location_name = models.CharField(max_length = 30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)

    def __str__(self):
        return self.location_name    
