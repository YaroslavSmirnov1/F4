from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from recipes.models import Recipe
from .serializers import RecipeSerializer


class RecipeListCreate(generics.ListCreateAPIView):
  queryset = Recipe.objects.all()
  serializer_class = RecipeSerializer