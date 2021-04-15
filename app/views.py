from django.shortcuts import render
from .models import My_Model
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def index(request):
    if request.method=='POST':
        print("Done and Dusted!")
        name = request.POST.get('name')
        img = request.FILES['image']
        c = My_Model(name=name, image = img)
        c.save()
        return render(request, "app/index.html")
    else:
        return render(request, "app/index.html")

def display(request):
    last_entry = My_Model.objects.last()
    context = {'last_entry': last_entry}
    return render(request, "app/display.html", context)