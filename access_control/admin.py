from django.contrib import admin
from .models import Role, ResourcePermission

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(ResourcePermission)
class ResourcePermissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'resource_name', 'can_view', 'can_create', 'can_edit', 'can_delete')
    list_filter = ('resource_name', 'can_view', 'can_create') # Фильтр справа для быстрого поиска
    search_fields = ('user__email', 'role__name', 'resource_name') # Поиск по почте пользователя, роли и ресурсу