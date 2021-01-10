from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def images(request):
    image = Images.objects.all()
    return render(request, 'image.html', {'image' : image})    


def search_category_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get('image')
        searched_images = Images.search_by_image_category(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{"message":message, "image":searched_images})

    else:
        message = "You haven't searched for any image category"  
        return render(request, 'search.html',{'message':message})

