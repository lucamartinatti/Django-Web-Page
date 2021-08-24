from django.shortcuts import render
from django.http import HttpResponse

# Homepage view
def index(request):
    return render(request, 'home_page.html', {})

# Results page view
def search_results(request):
    characteristic = request.GET['physique']
    return render(request, 'results_page.html', {'context': characteristic})
