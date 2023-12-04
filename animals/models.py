from django.db import models
# Create your models here.


class CatModel(models.Model):
    weight = models.JSONField(default=dict)
    name = models.CharField(max_length=50, primary_key=True)
    cfa_url = models.CharField(max_length=100)
    vetstreet_url = models.CharField(max_length=100)
    vcahospitals_url = models.CharField(max_length=100)
    temperament = models.CharField(max_length=400)
    origin = models.CharField(max_length=40)
    country_codes = models.CharField(max_length=20)
    country_code = models.CharField(max_length=4)
    description = models.CharField(max_length=1000)
    life_span = models.CharField(max_length=4)
    wikipedia_url = models.CharField(max_length=100)
    reference_image_id = models.CharField(max_length=15)
    left = models.JSONField(default=list)
    image_url = models.CharField(max_length=100)
    stars = models.JSONField(default=list)


class DogModel(models.Model):
    weight = models.JSONField(default=dict)
    height = models.JSONField(default=dict)
    name = models.CharField(max_length=50, primary_key=True)
    description = models.CharField(max_length=500)
    country_code = models.CharField(max_length=6)
    bred_for = models.CharField(max_length=50)
    breed_group = models.CharField(max_length=50)
    life_span = models.CharField(max_length=20)
    history = models.CharField(max_length=500)
    temperament = models.CharField(max_length=500)
    origin = models.CharField(max_length=40)
    reference_image_id = models.CharField(max_length=100)
    image = models.JSONField(default=dict)
