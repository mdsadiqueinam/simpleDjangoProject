from django.shortcuts import render

from .models import Pizza
# Create your views here.

def index(request) :
    pizzas = Pizza.objects.all().order_by('price')
    # pizzas_names_and_price = ["{} : {}$".format(item.name, item.price) for item in pizzas]
    # pizzas_names_and_price_str = ", ".join(pizzas_names_and_price)
    # return HttpResponse("Our Pizzas : "+pizzas_names_and_price_str)
    return render(request, 'menu/index.html', {'pizzas' : pizzas})