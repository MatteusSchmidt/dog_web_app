from django.urls import path
from . import views

# url patterns for every breed of dog and cat, including a default value of my favorite of each breed
urlpatterns = [
    path('cats/<str:name>/', views.cats_request, name='cat_detail'),
    path('cats/', views.cats_request, name='default_cat'),
    path('api/get_cats/', views.get_cats),
    path('dogs/<str:name>/', views.dogs_request, name='dog_detail'),
    path('dogs/', views.dogs_request, name='default_dog'),
    path('api/get_dogs/', views.get_dogs)
]

