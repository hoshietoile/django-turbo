from ..serializers import (
  UserRetrieveSerializer,
  UserCreateSerializer,
  UserUpdateSerializer,
)
from rest_framework import views
from utils.decorators import extend_res

class UsersView(views.APIView):

  @extend_res(res=UserRetrieveSerializer(many=True))
  def get(self): pass

  @extend_res(req=UserCreateSerializer, res=UserRetrieveSerializer)
  def post(self, req: UserCreateSerializer): pass

  @extend_res(req=UserUpdateSerializer, res=UserRetrieveSerializer)
  def put(self, req: UserUpdateSerializer): pass