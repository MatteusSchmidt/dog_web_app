from django.shortcuts import render, get_object_or_404
from .models import CatModel, DogModel
from .serializers import DogModelSerializer, CatModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def Home(request):
    return render(request, 'homepage.html')


# views which return cats and dogs
def cats_request(request, name='Savannah'):
    name = name.replace('%20', ' ')
    cat = get_object_or_404(CatModel, name=name)
    all_cats = CatModel.objects.all().values_list('name', flat=True)
    return render(request, 'cats.html', {'cat': cat, 'names_list': all_cats})


def dogs_request(request, name='Basset Hound'):
    name = name.replace('%20', ' ')
    dog = get_object_or_404(DogModel, name=name)
    all_dogs = DogModel.objects.all().values_list('name', flat=True)
    return render(request, 'dogs.html', {'dog': dog, 'names_list': all_dogs})


# API GET functions to return serialized data
@api_view(['GET'])
def get_dogs(request):
    # name = request.query_params.get('name')
    dogs = DogModel.objects.all()
    if dogs:
        serialized = DogModelSerializer(dogs, many=True)
        return Response(serialized.data)
    else:
        return Response({})


@api_view(['GET'])
def get_cats(request):
    cats = CatModel.objects.all()
    if cats:
        serialized = CatModelSerializer(cats, many=True)
        return Response(serialized.data)
    else:
        return Response({})
