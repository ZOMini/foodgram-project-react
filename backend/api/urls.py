from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CreateUserView, IngredientViewSet, TagViewSet

app_name = 'api'

router = DefaultRouter()
router.register('users', CreateUserView, basename='users')
router.register('tag', TagViewSet)
router.register('ingredient', IngredientViewSet)
# router.register('recipes', RecipeViewSet)
# router.register('users', FollowViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
