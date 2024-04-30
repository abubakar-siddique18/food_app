from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    process = models.TextField()
    image1 = models.ImageField(upload_to='RecipeImages')
    image2 = models.ImageField(upload_to='RecipeImages', null=True, blank=True)
    image3 = models.ImageField(upload_to='RecipeImages', null=True, blank=True)
    image4 = models.ImageField(upload_to='RecipeImages', null=True, blank=True)

    def __str__(self):
        return self.recipe_name
