# from drf_spectacular.utils import OpenApiExample, OpenApiParameter, extend_schema
from rest_framework import views, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from shop.models import Book
from utils.decorators import extend_res

from ..serializers import (
  BookPDFRequestSerializer,
  BookPDFResponseSerializer,
  BookSerializer,
)

class BookViewSet(viewsets.ModelViewSet):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

class BookPDFApiView(views.APIView):
  # queryset = Book.objects.all()
  # serializer_class = BookPDFRequestSerializer

  @extend_res(req=BookPDFRequestSerializer, res=BookPDFResponseSerializer)
  def post(self, request, pk, *args, **kargs) -> BookPDFResponseSerializer:
    book = Book.objects.all()
    request_serializer = self.get_serializer(instance=book, data=request.data)
    request_serializer.is_valid(raise_exception=True)

    download_url = "test.pdf"    
    response_serializer = BookPDFResponseSerializer(instance=book)
    response_serializer.instance.download_url = download_url
    return Response(response_serializer.data)
