from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home_page.html', {})

def search_results(request):
    characteristic = request.POST['physique']
    return render(request, 'results_page.html', {'context': characteristic})
