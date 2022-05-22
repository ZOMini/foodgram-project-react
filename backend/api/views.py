from djoser.views import UserViewSet
from rest_framework import filters, permissions, viewsets

from api.models import Ingredient, IngredientRecipe, Recipe, Tag, User
from api.permissions import AdminOrReadOnly
from api.serializers import (IngredientSerializer, RegistrationSerializer,
                             TagSerializer)


class CreateUserView(UserViewSet):
    serializer_class = RegistrationSerializer

    def get_queryset(self):
        return User.objects.all()

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AdminOrReadOnly,)
    pagination_class = None

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (AdminOrReadOnly,)
    pagination_class = None
    # filter_backends = (DjangoFilterBackend,)
    # filterset_class = IngredientSearchFilter
