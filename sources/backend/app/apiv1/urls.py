from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)

app_name = 'apiv1'
urlpatterns = [
  path('apitests', views.ApiTestView.as_view()),
  path('books/pdf', views.BookPDFApiView.as_view()),
  path('', include(router.urls)),
]
