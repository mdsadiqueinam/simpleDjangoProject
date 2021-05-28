from django.contrib import admin

# Register your models here.

#Custom class created to change the view of admin pizza menu in browser
class PizzaAdmin(admin.ModelAdmin) :
    list_display = ('name', 'ingredients', 'vegetarian', 'price')
    search_fields = ['name', 'price']

from .models import Pizza

admin.site.register(Pizza, PizzaAdmin)