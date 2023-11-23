from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import *
# Create your views here.
@api_view(["GET", "POST"])
def getAllCustomers(request):
    if request.method == "GET":         
        customers = Customers.objects.all()
        customersSerializers = CustomerSerializer(customers, many=True)
        return Response(customersSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        customerNuevo = CustomerSerializer(data = request.data)

        if customerNuevo.is_valid():
            customerNuevo.save()
            return Response(customerNuevo.data, status=status.HTTP_202_ACCEPTED)
        return Response(customerNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getCustomerById(request, pk):
    try:
        customer = Customers.objects.get(customerid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':

        request.data['customerid'] = pk


        if 'companyname' not in request.data:
            request.data['companyname'] = customer.companyname
        
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        # borrar el customer seleccionado y ademas borrar todas las Orders que dependan de ese customer
        customer.delete()
        return Response(status=status.HTTP_200_OK)
    
    # --- SUPPLIERS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllSuppliers(request):
    if request.method == "GET":         
        suppliers = Suppliers.objects.all()
        suppliersSerializers = SupplierSerializer(suppliers, many=True)
        return Response(suppliersSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        supplierNuevo = SupplierSerializer(data = request.data)
        if supplierNuevo.is_valid():
            supplierNuevo.save()
            return Response(supplierNuevo.data, status=status.HTTP_200_OK)
        return Response(supplierNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getSupplierById(request, pk):
    try:
        supplier = Suppliers.objects.get(supplierid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = SupplierSerializer(supplier)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['supplierid'] = pk
    
        serializer = SupplierSerializer(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        supplier.delete()
        return Response(status=status.HTTP_200_OK)

# --- CATEGORIES ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllCategories(request):
    if request.method == "GET":         
        categories = Categories.objects.all()
        categoriesSerializers = CategorieSerializer(categories, many=True)
        return Response(categoriesSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":

        categorieNuevo = CategorieSerializer(data = request.data)
        if categorieNuevo.is_valid():
            categorieNuevo.save()
            return Response(categorieNuevo.data, status=status.HTTP_200_OK)
        return Response(categorieNuevo.errors ,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET", "PUT", "DELETE"])
def getCategoryById(request, pk):
    try:
        categorie = Categories.objects.get(categoryid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = CategorieSerializer(categorie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        request.data['categoryid'] = pk
    
        serializer = CategorieSerializer(categorie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        categorie.delete()
        return Response(status=status.HTTP_200_OK)

# --- PRODUCTS ------------------------------------------------------------------------------------
@api_view(["GET", "POST"])
def getAllProducts(request):
    if request.method == "GET":         
        products = Products.objects.all()
        productSerializers = ProductSerializer(products, many=True)
        return Response(productSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        productNuevo = ProductSerializer(data=request.data)
        if productNuevo.is_valid():
            productNuevo.save()
            return Response(productNuevo.data, status=status.HTTP_200_OK)
        return Response(productNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getProductById(request, pk):
    try:
        product = Products.objects.get(productid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['productid'] = pk
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_200_OK)

# --- ORDERS ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllOrders(request):
    if request.method == "GET":         
        orders = Orders.objects.all()
        orderSerializers = OrderSerializer(orders, many=True)
        return Response(orderSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderNuevo = OrderSerializer(data=request.data)
        if orderNuevo.is_valid():
            orderNuevo.save()
            return Response(orderNuevo.data, status=status.HTTP_200_OK)
        return Response(orderNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getOrderById(request, pk):
    try:
        order = Orders.objects.get(orderid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_200_OK)

# --- ORDER_DETAILS ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllOrderDetails(request):
    if request.method == "GET":         
        order_details = Orderdetails.objects.all()
        orderDetailsSerializers = OrderdetailSerializer(order_details, many=True)
        return Response(orderDetailsSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        orderDetailNuevo = OrderdetailSerializer(data=request.data)
        if orderDetailNuevo.is_valid():
            orderDetailNuevo.save()
            return Response(orderDetailNuevo.data, status=status.HTTP_200_OK)
        return Response(orderDetailNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getOrderDetailById(request, pk):
    try:
        order_detail = Orderdetails.objects.get(orderid=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = OrderdetailSerializer(order_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['orderid'] = pk
        serializer = OrderdetailSerializer(order_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        order_detail.delete()
        return Response(status=status.HTTP_200_OK)

# --- EMPLOYEES ------------------------------------------------------------------------------------

@api_view(["GET", "POST"])
def getAllEmployees(request):
    if request.method == "GET":         
        employees = Employees.objects.all()
        employeeSerializers = EmployeeSerializer(employees, many=True)
        return Response(employeeSerializers.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        employeeNuevo = EmployeeSerializer(data=request.data)
        if employeeNuevo.is_valid():
            employeeNuevo.save()
            return Response(employeeNuevo.data, status=status.HTTP_200_OK)
        return Response(employeeNuevo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
def getEmployeeById(request, pk):
    try:
        employee = Employees.objects.get(employee_id=pk)
    except Exception:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        request.data['employee_id'] = pk
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_200_OK)

# ---------------------------------------- PRUEBAS -------------------------------------------

@api_view(["POST"])
def create_order_with_details(request):
    order_serializer = OrderSerializer(data=request.data)
    if order_serializer.is_valid():
        order = order_serializer.save()
        order_details_data = request.data.get('order_details', [])
        for order_detail_data in order_details_data:
            order_detail_data['order'] = order.id
            order_detail_serializer = OrderdetailSerializer(data=order_detail_data)
            
            if order_detail_serializer.is_valid():
                order_detail_serializer.save()
            else:
                order.delete()
                return Response(order_detail_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
    return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_orders_with_details(request):
    orders = Orders.objects.all()
    order_serializer = OrderSerializer(orders, many=True)
    return Response(order_serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def punto1(request):

    supplierid = request.query_params.get("supplierid")
    categoryid = request.query_params.get("categoryid")
    stockmin = request.query_params.get("stockmin")
    productosFiltrados = Products.objects.filter(supplierid  = supplierid, categoryid = categoryid)
    resultados = []
    if not productosFiltrados:
        return Response(status=status.HTTP_404_NOT_FOUND)
    for p in productosFiltrados:
        suma = p.unitsinstock + p.unitsonorder
        if suma < int(stockmin) and p.discontinued != 1:
            resultado = {
                "ProductId" : p.productid,
                "ProductName" : p.productname,
                "StockFuturo" : f"{suma} - ${p.unitprice}"
            }
            resultados.append(resultado)
    if not resultados:
        return Response(status=status.HTTP_204_NO_CONTENT)

    productoSerializer = ProductoSerializer(resultados, many=True)
    return Response(productoSerializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def punto2(request):
    supplierid = request.data["supplierid"]
    categoryid = request.data["categoryid"]
    requiredStock = request.data["requiredStock"]
    customerid = request.data["customerid"]
    employeeid = request.data["employeeid"]
    
    products = Products.objects.filter(supplierid = supplierid, categoryid = categoryid)
        
    order = {
        "customerid" : customerid,
        "employeeid" : employeeid,
    }
    orderDetails = []
    for p in products:
        suma = p.unitsinstock + p.unitsonorder
        if suma < requiredStock:
            orderDetail = {
                "productid" : p.productid,
                "unitprice" : p.unitprice,
                "quantity" : p.calcularDiferenciaDeStock(requiredStock)
    
            }
            if orderDetail["quantity"] <= 100:
                orderDetail["discont"] = 0
            else:
                orderDetail["discont"] = 0.1
    return Response({"todo": "ok"})