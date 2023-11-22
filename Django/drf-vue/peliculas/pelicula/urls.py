from django.urls import path
from .views import CategoryViewSet, FilmViewSet, ListCreateUser, Login, RetrieveUpdateDestroyUser
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('films', FilmViewSet, basename='films')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = router.urls + [
    path('list-create-user/', ListCreateUser.as_view(), name='list-create-user'),
    path('login/', Login.as_view(), name='login'),
    path('retrieve-update-destroy-user/<int:pk>/', RetrieveUpdateDestroyUser.as_view(), name='retrieve-update-destroy-user'),
]