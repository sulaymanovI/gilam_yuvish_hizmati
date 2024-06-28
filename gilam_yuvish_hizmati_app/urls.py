from django.urls import path
from .views import buyurtma_olish

urlpatterns = [
    path('',buyurtma_olish,name='buyurtma_olish'),
]
