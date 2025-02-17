from rest_framework.permissions import BasePermission

class IsAuthenticatedOrGuest(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        
        if request.query_params.get('email') == 'guest@example.com':
            return True
        
        return False
    
    
 