# from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import views
from rest_framework.response import Response
from shop.models import Book
from utils.decorators import extend_res

from ..serializers import (
  BookSerializer,
)

class ApiTestView(views.APIView):
  @extend_res(req=BookSerializer, res=BookSerializer(many=True))  
  def get(self, request):
    """Get a List of Book"""
    query = Book.objects.all()
    serializer = BookSerializer(query, many=True)
    return Response(serializer.data)

