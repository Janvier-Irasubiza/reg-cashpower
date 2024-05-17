from django.contrib import admin
from .models import User, Client, Request, Upload, Dispense

admin.site.register([User, Client, Request, Upload, Dispense])