from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import MenuCategory
from .serializers import MenuCategorySerializer

# Create your views here.
class MenuCategoryListView(ListAPIView):
    """
    returns a list of all available menu categories
    """
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
