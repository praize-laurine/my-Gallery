from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def images(request):
    image = Images.objects.all()
    return render(request, 'image.html', {'image' : image})    
