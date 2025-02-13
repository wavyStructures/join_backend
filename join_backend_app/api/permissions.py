from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsGuestOrReadOnly(BasePermission):    
    """
    Custom permission to grant read-only access to guest users.
    """
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return request.method in SAFE_METHODS
        
        if request.user.is_guest:
            return request.method in SAFE_METHODS  # Allow only GET, HEAD, OPTIONS for guest
        return True
    

