from django.urls import path, include
from rest_framework import routers
# from .views.users_view import UsersView
# from .views.books_view import BookViewSet, BookPDFApiView
# from .views.apitest_view import ApiTestView
from .views import (
  BookPDFApiView,
  BookViewSet,
  ApiTestView,
  UsersView,
)

router = routers.DefaultRouter()
router.register('books', BookViewSet)

app_name = 'apiv1'
urlpatterns = [
  path('apitests', ApiTestView.as_view()),
  path('users', UsersView.as_view()),
  path('books/pdf', BookPDFApiView.as_view()),
  path('', include(router.urls)),
]
