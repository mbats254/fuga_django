from django.contrib import admin
from .models import Farmers, Animals, Breeds, Farmers_Animals, Farm, Visits
# Register your models here.
admin.site.register(Farmers)
admin.site.register(Animals)
admin.site.register(Breeds)
admin.site.register(Farmers_Animals)
admin.site.register(Farm)
admin.site.register(Visits)