from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import TagViewSet

app_name = 'api'

router = DefaultRouter()
router.register('tags', TagViewSet)
# router.register('ingredients', IngredientsViewSet)
# router.register('recipes', RecipeViewSet)
# router.register('users', FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
