from django.conf import settings

def display_maintenance_page(request):
    """
    Overridable hook function to determine if the maintenance mode page should be displayed.
    
    Returns True if the maintenance mode page should be displayed
    """
    # Allow access if remote ip is in INTERNAL_IPS
    if request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
        return False
    
    # Allow acess if the user doing the request is logged in and a
    # staff member.
    if hasattr(request, 'user') and request.user.is_staff:
        return False
        
    return True

MAINTENANCE_MODE = getattr(settings, 'MAINTENANCE_MODE', False)
DISPLAY_MAINTENANCE_PAGE = getattr(settings, 'DISPLAY_MAINTENANCE_PAGE', display_maintenance_page)
MAINTENANCE_PAGE_CONTEXT = getattr(settings, 'MAINTENANCE_PAGE_CONTEXT', {})
