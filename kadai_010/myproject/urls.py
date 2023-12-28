from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/', views.ProductListView.as_view(), name="list"),
    path('crud/detail/<int:pk>', views.ProductDetailView.as_view(), name="detail"),
    path('', views.TopView.as_view(), name="top"),
]
