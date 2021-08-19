from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world..")
    #return render(request, 'home_page.html', {})

def search_results(request):
    return render(request, 'results_page.html',{})