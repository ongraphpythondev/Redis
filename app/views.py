from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views import View
from app.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app.forms import ProductForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from django.core.cache import cache


# Create your views here.

@method_decorator(csrf_exempt, name= "dispatch")
class Add(FormView):
    template_name = "app/add.html"
    form_class = ProductForm
    success_url = '/home/'

    def form_valid(self, form):
        # print(form["price"], form["name"])
        Product.objects.create(name = form.cleaned_data['name'], price = form.cleaned_data['price'], description = form.cleaned_data["description"])
        return super().form_valid(form)
    
    def form_invalid(self, form):
        print("form is invalid")
        return render(self.request, "app/add.html")

@method_decorator(csrf_exempt, name= "dispatch")
class Home(View):

    def get(self, request):
        filter_product = request.GET.get("product")
        if cache.get(filter_product):
            print("data came from caches")
            products = cache.get(filter_product)
            print(cache.get(filter_product))
        else:
            if filter_product:
                products = Product.objects.filter(name__contains = filter_product)
                cache.set(filter_product, products)
                print("data came from DB")
            else:
                print("data came from DB")
                products = Product.objects.all()

        return render(request, "app/home.html", {"products" :products})
    
