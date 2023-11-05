from rest_framework import serializers
from shop.models import Book


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