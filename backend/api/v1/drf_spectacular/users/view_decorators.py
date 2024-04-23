from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status

from api.v1.drf_spectacular.serializers import (Response400Serializer,
                                                Response401Serializer)
from api.v1.users.serializers import (InviteCodeActivateSerializer,
                                      UserSerializer)

USERS_VIEW_DECORATORS = {
    "ActivateInviteCodeView": extend_schema_view(
        post=extend_schema(
            tags=("users",),
            request=InviteCodeActivateSerializer,
            responses={
                status.HTTP_200_OK: InviteCodeActivateSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "UserView": extend_schema_view(
        get=extend_schema(
            tags=("users",),
            request=UserSerializer,
            responses={
                status.HTTP_200_OK: UserSerializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
    "UpdateUserView": extend_schema_view(
        patch=extend_schema(
            tags=("users",),
            request=UserSerializer,
            responses={
                status.HTTP_200_OK: UserSerializer,
                status.HTTP_400_BAD_REQUEST: Response400Serializer,
                status.HTTP_401_UNAUTHORIZED: Response401Serializer,
            },
        ),
    ),
}
