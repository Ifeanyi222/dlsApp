from django.urls import path
from . import views

urlpatterns = [
    # URL for listing stock
    path('stock/', views.stock_list, name='stock_list'),

    # URL for adding stock
    path('stock_add/', views.add_stock, name='add_stock'),

    # URL for processing sales via the POS interface
    path('pos/', views.process_sale, name='pos'),

    # Optional: Add a summary or list of sales
    path('sales_summary/', views.sales_summary, name='sales_summary'),
]


