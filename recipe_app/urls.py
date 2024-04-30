from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('recipe/', views.recipe_list, name="recipe_list"),
    path('create/', views.recipe_create, name='recipe_create'),
    path('<int:id>detail/', views.recipe_detail, name='details'),
    path('login/', views.login_page, name='user_login'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('login/register/', views.register, name='user_register'),
]

