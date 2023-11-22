from rest_framework import serializers
import django_filters as filters
from .models import Category, Film, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FilmFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name='category', lookup_expr='exact')
    title = filters.CharFilter(method='filter_by_search', lookup_expr='icontains')
    
    def filter_by_search(self, queryset, value):
        return queryset.filter(title__icontains=value) | queryset.filter(description__icontains=value) | queryset.filter(publication__icontains=value)
        
    class Meta:
        model = Film
        fields = {
            'category': ['exact'],
            'title': ['icontains']
        }

class FilmSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = Film
        fields = '__all__'
        filterset_class = FilmFilter
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'