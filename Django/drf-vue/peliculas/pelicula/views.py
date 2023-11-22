from .models import Category, Film, User
from .serializers import CategorySerializer, FilmSerializer, UserSerializer
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id})

class ListCreateUser(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.filter(user=self.request.user)

class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        #Filtrado por categoria
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        #Filtrado por nombre dde producto
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(description__icontains=search) | queryset.filter(publication__icontains=search)

        return queryset
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer