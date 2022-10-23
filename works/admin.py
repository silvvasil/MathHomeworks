from django.contrib import admin
from .models import Task, Work


admin.site.register(Task)
admin.site.register(Work)

# @admin.register(Work)
# class WorkAdmin(admin.ModelAdmin):
    # list_display = ('description', 'work_image', 'comment')
    # readonly_fields = ('description', 'work_image')



# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     fields = (('name', 'venue'), 'event_date', 'description', 'manager')
#     list_display = ('name', 'event_date', 'venue')
#     list_filter = ('event_date', 'venue')
#     ordering = ('-event_date',)

# # Register your models here.
