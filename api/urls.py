from django.urls import path, include
from .views import *

urlpatterns = [
    path("customer/", getAllCustomers, name="getAllCustomers"),
    path("customer/<str:pk>", getCustomerById , name="getCustomerById"),

    path("supplier/", getAllSuppliers, name="getAllSuppliers"),
    path("supplier/<str:pk>", getSupplierById , name="getSupplierById"),

    path("category/", getAllCategories, name="getAllCategories"),
    path("category/<str:pk>", getCategoryById , name="getCategoryById"), 

    path("product/", getAllProducts, name="getAllProducts"),
    path("product/<str:pk>", getProductById , name="getProductById"), 

    path("order/", getAllOrders, name="getAllOrders"),
    path("order/<str:pk>/", getOrderById, name="getOrderById"),

    path("orderdetail/", getAllOrderDetails, name="getAllOrderDetails"),
    path("orderdetail/<str:pk>/", getOrderDetailById, name="getOrderDetailById"),

    path("employees/", getAllEmployees, name="getAllEmployees"),
    path("employees/<str:pk>/", getEmployeeById, name="getEmployeeById"),

    path("productos/", punto1),
    path("orders/", punto2)
    
]