from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_email', 'country',
                    'user_date_joined', 'user_last_login']
    search_fields = ['user', 'user__user__email', 'country']

    @admin.display(ordering='user__user__email')
    def user_email(self, data):
        return data.user.user.email

    @admin.display(ordering='user__user__date_joined')
    def user_date_joined(self, data):
        return data.user.user.date_joined

    @admin.display(ordering='user__user__last_login')
    def user_last_login(self, data):
        return data.user.user.last_login
