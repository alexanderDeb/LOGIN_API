from django.shortcuts import redirect
from requests import request


class SuperUserMixin(object):
    def dispatch(self, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        return redirect