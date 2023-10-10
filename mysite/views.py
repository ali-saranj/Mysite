from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def Home(request):
    context = {
        'mymembers': "",
    }
    return HttpResponse(loader.get_template('index.html').render(context,request))
