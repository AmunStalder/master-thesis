from django.contrib import admin
from .models import Productions, Ingredient, AMBVValue
# Register your models here.
admin.site.register(Productions)
admin.site.register(Ingredient)
admin.site.register(AMBVValue)
