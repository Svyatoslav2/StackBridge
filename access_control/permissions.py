from rest_framework import permissions
from .models import ResourcePermission

class CustomAccessPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # 1. Если не залогинен или не активен -> 401
        if not request.user or not request.user.is_authenticated or not request.user.is_active:
            return False

        # 2. Суперюзер имеет доступ ко всему
        if request.user.is_superuser:
            return True

        # 3. Определяем, какой ресурс запрашивается
        resource_name = getattr(view, 'resource_name', request.path.strip('/').split('/')[0])
        
        action_map = {
            'GET': 'can_view', 'POST': 'can_create',
            'PUT': 'can_edit', 'PATCH': 'can_edit', 'DELETE': 'can_delete'
        }
        required_action = action_map.get(request.method, 'can_view')

        # 4. Проверяем в БД наличие права
        has_perm = ResourcePermission.objects.filter(
            user=request.user,
            resource_name=resource_name,
            **{required_action: True}
        ).exists()

        return has_perm # Если False, Django вернет 403