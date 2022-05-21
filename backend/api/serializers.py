from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
from users.models import User

from api.models import Ingredient, IngredientRecipe, Recipe, Tag


class RegistrationSerializer(UserCreateSerializer):
    """
    Создание сериализатора модели пользователя.
    """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    class Meta:
        """
        Мета параметры сериализатора модели пользователя.
        """
        model = User
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

class TagSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Tag


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         read_only=True, slug_field='username'
#     )

#     class Meta:
#         fields = '__all__'
#         model = Comment


# class GroupSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Group
#         fields = '__all__'


# class FollowSerializer(serializers.ModelSerializer):
#     user = serializers.SlugRelatedField(
#         queryset=User.objects.all(),
#         default=serializers.CurrentUserDefault(),
#         slug_field='username'
#     )
#     following = serializers.SlugRelatedField(
#         queryset=User.objects.all(),
#         slug_field='username'
#     )

#     class Meta:
#         fields = ('user', 'following')
#         model = Follow
#         validators = [
#             UniqueTogetherValidator(
#                 queryset=Follow.objects.all(),
#                 fields=('user', 'following')
#             )
#         ]
#     # Pytest говорит надо проверять!.

#     def validate(self, data):
#         if data['user'] == data['following']:
#             raise serializers.ValidationError(
#                 'Нельзя подписаться на себя!'
#             )
#         return data
