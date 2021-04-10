from django.contrib import admin

# Register your models here.
from hospitalapp.models import Doctor, Deprt

admin.site.register(Doctor)
admin.site.register(Deprt)