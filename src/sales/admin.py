from django.contrib import admin
from .models import Position
from .models import Sale 
from .models import CSV
# Register your models here.
admin.site.register(Position)
admin.site.register(Sale)
admin.site.register(CSV)
