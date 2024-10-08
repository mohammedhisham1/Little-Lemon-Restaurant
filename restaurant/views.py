# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views

from . import models

def menu(request):
    menu_data = models.Menu.objects.all()
    main_data = {"menu" : menu_data}
    return render(request,'menu.html',main_data)


def display_menu_items(request,  pk=None) :
    if pk :
        menu_item = models.Menu.objects.get(pk=pk)

    else:
        menu_item = ''

    context = {'menu_item': menu_item}

    return render(request,'menu_item.html',context)
