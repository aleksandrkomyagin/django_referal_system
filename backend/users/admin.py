from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "username")
    fields = (
        "username", "first_name",
        "last_name", "phone_number",
        "invite_code", "inviter",
    )
    readonly_fields = ("invite_code",)
    empty_value_display = "-пусто-"


admin.site.register(User, UserAdmin)
