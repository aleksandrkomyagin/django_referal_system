from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import exceptions, serializers, status

from .utils import get_invite_code

User = get_user_model()


class BaseSerializerPhoneNumber(serializers.Serializer):
    phone_number = PhoneNumberField(region=settings.NUMBER_REGION)


class SignupSerializer(BaseSerializerPhoneNumber):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def validate(self, attrs):
        phone_number = attrs["phone_number"]

        try:
            self.user, created = User.objects.get_or_create(phone_number=phone_number)
        except Exception as e:
            raise exceptions.ValidationError({"error": e})

        if created:
            invite_code = get_invite_code()
            self.user.invite_code = invite_code
            self.user.save(update_fields=["invite_code"])

        return attrs


class ConfirmSignUpView(BaseSerializerPhoneNumber):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    confirmation_code = serializers.CharField(required=True)

    def validate(self, attrs):
        phone_number = attrs["phone_number"]
        self.user = get_object_or_404(User, phone_number=phone_number)

        cached_confirm_code = cache.get(str(phone_number), None)
        if cached_confirm_code is None:
            raise exceptions.ValidationError(
                {"message": "Срок действия кода истек, запросите новый."},
                code=status.HTTP_400_BAD_REQUEST,
            )

        confirmation_code = attrs["confirmation_code"]
        if cached_confirm_code != confirmation_code:
            raise exceptions.ValidationError(
                {"message": "Неверный код подтверждения."},
                code=status.HTTP_400_BAD_REQUEST,
            )

        cache.set(str(phone_number), None)

        return attrs
