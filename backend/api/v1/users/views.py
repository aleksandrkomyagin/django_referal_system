from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.drf_spectacular.custom_decorators import \
    get_drf_spectacular_view_decorator
from api.v1.users.serializers import (InviteCodeActivateSerializer,
                                      UserSerializer)

User = get_user_model()


class BaseView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


@get_drf_spectacular_view_decorator("users")
class UserView(BaseView):

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@get_drf_spectacular_view_decorator("users")
class ActivateInviteCodeView(BaseView):
    serializer_class = InviteCodeActivateSerializer

    def post(self, request):
        serializer = self.get_serializer(
            request.user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(**{"inviter": serializer.inviter})
        return Response(
            {"invite_code": "Инвайт-код активирован."},
            status=status.HTTP_200_OK,
        )


@get_drf_spectacular_view_decorator("users")
class UpdateUserView(BaseView):

    def patch(self, request):
        serializer = self.get_serializer(
            request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
