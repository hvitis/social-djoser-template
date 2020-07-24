from .models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib import admin
from accounts.models import UserProfile
from django.contrib.gis.db import models
from django.contrib import admin


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "User's Profile"
    list_display = ("id")


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""
    inlines = (ProfileInline, )
    readonly_fields = ('date_joined', 'unique_id')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
     
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'nickname',
                    'date_joined', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'nickname',
                     'date_joined', 'first_name', 'last_name')
    ordering = ('email',)
