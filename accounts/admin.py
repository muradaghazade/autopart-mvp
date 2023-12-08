from django.contrib import admin
from accounts.models import User, Request, Offer 

admin.site.register([User, Request, Offer])
