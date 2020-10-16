from django.contrib import admin
from YourThoughts.models import Registration
from firstsite.urls import urlpatterns

# Register your models here
@admin.register(Registration)
class Useradmin(admin.ModelAdmin):
    pass
