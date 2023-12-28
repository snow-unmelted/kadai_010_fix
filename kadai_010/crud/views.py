from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductDetailView(DetailView):
    model = Product

class TopView(TemplateView):
    template_name = "top.html"