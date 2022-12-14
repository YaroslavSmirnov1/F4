from django.urls import path
from . views import RecipeList


urlpatterns = [
  path('', RecipeList.as_view()),
  path('recipe/<slug:slug>/', RecipeList.as_view()),
  path('category/<slug:slug>/', RecipeList.as_view()),
]