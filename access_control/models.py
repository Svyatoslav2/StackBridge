from django.db import models
from django.conf import settings


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ResourcePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    resource_name = models.CharField(max_length=100) # например "blog", "documents"
    
    can_view = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

class Meta:
    unique_together = [['role', 'resource_name'], ['user', 'resource_name']]

    def __str__(self):
        return f"{self.user or self.role} - {self.resource_name}"