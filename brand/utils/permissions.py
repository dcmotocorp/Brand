from rest_framework import permissions 
from auths.models import User
from apis.models import Startups

class IsSuperAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print("=============================")
        
        if request.user:
            user_instantce = Startups.objects.filter(user=request.user).first()
            print(user_instantce,"====================ytestst")
            if user_instantce:
                pk = request.parser_context.get('kwargs').get('pk')
                if user_instantce.id == pk:
                    return True
        
        elif request.method in permissions.SAFE_METHODS:
            print(request.parsers,"====================================")
            return True
        return request.user.is_superuser
        
class IsSelfOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj==request.user
    
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return obj.user==request.user      
    
class IsActiveOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj,'is_active')

class IsAmbasador(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role==CustomUser.AMBASADOR:
            return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if request.user.role==CustomUser.AMBASADOR:
            return True
        else:
            return False
    
class IsPublic(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role==CustomUser.PUBLIC:
            return True
        else:
            return False