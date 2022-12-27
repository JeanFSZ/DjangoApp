from django.contrib import admin
from room.models import Room, Alert
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    pass

class AlertAdmin(admin.ModelAdmin):
    pass

admin.site.register(Room,RoomAdmin)
admin.site.register(Alert,AlertAdmin)