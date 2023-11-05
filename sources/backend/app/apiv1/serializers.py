from rest_framework import serializers
from shop.models import Book, User, Auth


class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = ['id', 'title', 'price']
    # TODO: エラーメッセージ生成処理の共通化?
    extra_kwargs = {
      'title': {
        'error_messages': {
          'blank': "Don't make the title blank.",
        }
      },
      'price': {
        'error_messages': {
          'invalid': 'Please input the valid integer in the Price field.',
        }
      },
    }

class BookPDFRequestSerializer(serializers.ModelSerializer):
  size = serializers.ChoiceField(choices=['B5', 'A4'])

  class Meta:
    model = Book
    fields = ['title', 'price', 'size']

class BookPDFResponseSerializer(serializers.ModelSerializer):
  download_url = serializers.URLField()

  class Meta:
    model = Book
    exclude = ['created_at']

class AuthRetrieveSerializer(serializers.ModelSerializer):
  class Meta:
    model = Auth
    fields = [
      'id',
      'name',
    ]

class UserRetrieveSerializer(serializers.ModelSerializer):
  auths = AuthRetrieveSerializer(many=True, read_only=True)
  class Meta:
    model = User
    fields = ['id', 'name', 'email', 'auths']

class UserCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['name', 'email', 'password', 'password_confirm']

class UserUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['name', 'email', 'password', 'password_confirm']