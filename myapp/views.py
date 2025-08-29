from django.shortcuts import render
from .models import *

# Create your views here.

def Homepage(request):
    mainslider = MainSliderModel.objects.all()
    about_five = AboutFiveModel.objects.all()
    about_service = AboutServiceModel.objects.all()
    contex = {
        'mainslider':mainslider,
        'about_five':about_five,
        'about_service':about_service

    }
    return render(request, 'index.html',contex)