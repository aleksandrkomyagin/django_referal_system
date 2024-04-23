from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from api.v1.auth.serializers import ConfirmSignUpView, SignupSerializer
from api.v1.drf_spectacular.serializers import (Response400Serializer,
                                                Response401Serializer)

AUTH_VIEW_DECORATORS = {
    "UserSignupView": extend_schema_view(
        post=extend_schema(
            tags=("auth",),
            request=SignupSerializer,
            responses={
                status.HTTP_200_OK: SignupSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "ConfirmSignUpView": extend_schema_view(
        post=extend_schema(
            tags=("auth",),
            request=ConfirmSignUpView,
            responses={
                status.HTTP_200_OK: TokenRefreshSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
            },
        ),
    ),
}
