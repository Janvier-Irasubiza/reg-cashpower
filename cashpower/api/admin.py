from django.contrib import admin
from .models import User, Request, Upload, RequestHandle, Dispense

admin.site.register([User, Request, Upload, RequestHandle, Dispense])