from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from apis.login.models import User

admin.site.register(User)
admin.site.register(Permission)
admin.site.register(ContentType)
