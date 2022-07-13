from django.shortcuts import redirect
from crum import get_current_request
from requests import request

class SuperUserMixin(object):
    
    request = get_current_request

    def dispatch(self, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return redirect