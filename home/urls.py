from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.index, name='home-page'),
    path('search_results/', views.search_results, name='search-results'),
]