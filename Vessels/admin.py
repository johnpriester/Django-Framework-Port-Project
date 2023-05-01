from django.contrib import admin
from .models import Vessel, VesselSchedule, PortCall
# Register your models here.


admin.site.register(Vessel)


class PortCallInlineAdmin(admin.StackedInline):
    model = PortCall
    extra = 2


class VesselScheduleAdmin(admin.ModelAdmin):
    fields = ['vessel', 'voyage_number']
    inlines = [PortCallInlineAdmin]


admin.site.register(VesselSchedule, VesselScheduleAdmin)

