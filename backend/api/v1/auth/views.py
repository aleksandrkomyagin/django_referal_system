from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework import status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .tasks import send_sms_task
from .utils import get_confirmation_code
from api.v1.auth import serializers
from api.v1.drf_spectacular.custom_decorators import \
    get_drf_spectacular_view_decorator

User = get_user_model()


@get_drf_spectacular_view_decorator("auth")
class UserSignupView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = serializers.SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data["phone_number"]
        confirmation_code = get_confirmation_code()
        cache.set(str(phone_number), confirmation_code)

        send_sms_task.delay(str(phone_number), confirmation_code)
        print(confirmation_code)

        return Response(serializer.data, status=status.HTTP_200_OK)


@get_drf_spectacular_view_decorator("auth")
class ConfirmSignUpView(views.APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = serializers.ConfirmSignUpView(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = RefreshToken.for_user(serializer.user)
        return Response(
            {"access": str(token.access_token), "refresh": str(token)},
            status=status.HTTP_200_OK,
        )
