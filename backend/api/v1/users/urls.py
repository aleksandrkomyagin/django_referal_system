from django.urls import path

from api.v1.users.views import ActivateInviteCodeView, UpdateUserView, UserView

urlpatterns = [
    path("me/", UserView.as_view(), name="me"),
    path(
        "activate_invite_code/",
        ActivateInviteCodeView.as_view(),
        name="activate_invite_code"
    ),
    path("change_me/", UpdateUserView.as_view(), name="change_me"),
]
