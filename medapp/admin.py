from django.contrib import admin
from medapp.models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Staff)
admin.site.register(Ward)
admin.site.register(Appointments)
admin.site.register(Contact)
