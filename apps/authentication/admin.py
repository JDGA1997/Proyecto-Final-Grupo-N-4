from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Perfil', {'fields': ('tipo_perfil',)}),
    )
    list_display = ('username', 'email', 'tipo_perfil', 'is_staff', 'is_active')
    list_filter = UserAdmin.list_filter + ('tipo_perfil',)

admin.site.register(User, CustomUserAdmin)