from rest_framework import filters, permissions, viewsets

from api.models import Ingredient, IngredientRecipe, Recipe, Tag, User
from api.permissions import AdminOrReadOnly
from api.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # pagination_class = LimitOffsetPagination
    permission_classes = (AdminOrReadOnly,)
