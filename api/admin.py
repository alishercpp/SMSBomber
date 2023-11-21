from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from unfold.admin import ModelAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm
from .models import User, Device


@admin.register(User)
class StudentAdmin(UserAdmin, ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['username', 'token', 'first_name', 'last_name', 'middle_name', 'is_free', 'end_date']
    fieldsets = (
        ('Mijozni tahrirlash', {
            'fields': ('username', 'first_name', 'last_name', 'middle_name', 'is_free'),
        }),
    )
    add_fieldsets = (
        ('Yangi mijoz qo\'shish', {
            "classes": ("wide", ),
            "fields": (
                'username', 'password1', 'password2',
                'first_name', 'last_name', 'middle_name', 'is_free',
            ),
        }),
    )
    search_fields = ("username", 'first_name', 'last_name', 'middle_name', )
    ordering = ('username', )

admin.site.unregister(Group)

admin.site.register(Device, ModelAdmin)