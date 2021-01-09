from django.test import TestCase
from .models import *

# Create your tests here.
class ImagesTestClass(TestCase):
    
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

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name = 'home')
        self.category.save_category_name()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category = Category(name = 'Food')
        self.category.save_category_name()

    def test_delete_category(self):
        self.category = Category(name = 'Food')
        self.category.save_category_name()
        self.category.save_category_name()

    def tearDown(self):
        Category.objects.all().delete()            

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(location_name='Kinoo')
        self.location.save_location_name()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location)) 

    def test_save_location(self):
        self.location.save_location_name()
        locations = Location.objects.all()
        print(locations)
        self.assertTrue(len(Locations)==1)    

    def test_update_location(self):
        new_location.update_location(self.location.id,new_location_name)
        updated_location = Location.objects.filter(location_name='Thika')
        self.assertTrue(len(updated_location) > 0)

    def test_delete_location(self):
        self.location.delete_location_name()
        locations = Location.objects.all()
        print(locations)
        self.assertTrue(len(Locations)==0)    
    




