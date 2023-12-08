from django.contrib import admin
from core.models import Make, Model, Part, Category

admin.site.register([Make, Model, Part,Category ])
# Register your models here.
