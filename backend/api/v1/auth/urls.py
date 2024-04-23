from django.urls import path

from api.v1.auth.views import ConfirmSignUpView, UserSignupView

urlpatterns = [
    path("signup/", UserSignupView.as_view(), name="signup"),
    path(
        "confirmation_signup/",
        ConfirmSignUpView.as_view(),
        name="confirmation_signup"
    ),
]
