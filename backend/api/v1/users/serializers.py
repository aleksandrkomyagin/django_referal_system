from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    invitings = serializers.StringRelatedField(
        many=True, read_only=True
    )
    invited_by_code = serializers.ReadOnlyField(
        source="inviter.invite_code",
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "phone_number",
            "email",
            "invite_code",
            "invited_by_code",
            "invitings",
        )

        read_only_fields = (
            "invitings",
            "invited_by_code",
            "invite_code",
        )


class InviteCodeActivateSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.inviter = None

    invite_code = serializers.CharField(required=True)

    def validate(self, attrs):
        invite_code = attrs["invite_code"]

        self.inviter = User.objects.get(invite_code=invite_code)
        if self.inviter is None:
            raise ValidationError({"invite_code": "Неверный инвайт-код."})

        if self.instance.invite_code == invite_code:
            raise ValidationError(
                {
                    "invite_code":
                    "Недопустимо использовать собственный инвайт-код"
                }
            )

        if self.instance.inviter:
            raise ValidationError(
                {"invite_code": "Вы уже активировали один инвайт-код."}
            )

        return attrs

    def save(self, **kwargs):
        self.instance.inviter = kwargs["inviter"]
        self.instance.save()
