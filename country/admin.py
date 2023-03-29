from django.contrib import admin
from . models import People , Custom , Event , Food
# Register your models here.
admin.site.register(People)
admin.site.register(Custom)
admin.site.register(Event)
admin.site.register(Food)
