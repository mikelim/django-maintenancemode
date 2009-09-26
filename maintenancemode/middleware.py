from django.conf import settings
from django.core import urlresolvers

from django.conf.urls import defaults
defaults.handler503 = 'maintenancemode.views.defaults.temporary_unavailable'
defaults.__all__.append('handler503')

from maintenancemode.conf.settings import MAINTENANCE_MODE, DISPLAY_MAINTENANCE_PAGE

class MaintenanceModeMiddleware(object):
    def process_request(self, request):
        # Allow access if middleware is not activated
        if not MAINTENANCE_MODE:
            return None

        if not DISPLAY_MAINTENANCE_PAGE(request):
            return None
        
        # Otherwise show the user the 503 page
        resolver = urlresolvers.get_resolver(None)
        
        callback, param_dict = resolver._resolve_special('503')
        return callback(request, **param_dict)
