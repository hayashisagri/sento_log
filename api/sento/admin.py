from django.contrib import admin

from .models import Sento, Area, UserSentoVisit


admin.site.register(Sento)
admin.site.register(Area)
admin.site.register(UserSentoVisit)
