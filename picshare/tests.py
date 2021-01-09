from django.test import TestCase
from .models import *

# Create your tests here.
class ImagesTestCase(TestCase):
    
    # Set up method
    def setUp(self):
        self.location = Location(name = 'Nakuru')
        self.location.save()

        self.category = Category(name = 'Adventure')
        self.category.save()

        self.new_image = Images(name = 'image', description = 'this is a nice image', location = self.location, category = self.category)
        self.new_image.save()

    def tearDown(self):
        Images.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()    


