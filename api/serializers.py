
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Customers, Suppliers, Categories, Products, Orders, Orderdetails, Employees
from .models import Customers

class SerializadorPadre(ModelSerializer):
    class Meta:
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class SupplierSerializer(SerializadorPadre):
    class Meta:
        model = Suppliers
        fields = '__all__'

class CategorieSerializer (SerializadorPadre):
   class Meta:
      model = Categories
      fields = '__all__'

class ProductSerializer (SerializadorPadre):
   class Meta:
      model = Products
      fields = '__all__'

class OrderdetailSerializer (SerializadorPadre):
   class Meta:
      model = Orderdetails
      fields = '__all__'

class OrderSerializer(SerializadorPadre):
   order_details = OrderdetailSerializer(many=True, read_only=True)

   class Meta:
      model = Orders
      fields = '__all__'

class EmployeeSerializer (SerializadorPadre):
   class Meta:
      model = Employees
      fields = '__all__'

#class Punto1Serializer(serializers.Serializer):
#   id = serializers.IntegerField()
#   apellido = serializers.CharField()
#   nombre = serializers.CharField()
#   birthdate = serializers.DateTimeField()
#@api_view(["GET"])
#def punto1(request):
#    letra = request.query_params.get("letter")
#    year = request.query_params.get("year")
#
#    empleadosFiltrados = Employees.objects.filter(firstname__icontains = letra)
#    resultados = []
#    for e in empleadosFiltrados:
#        resultado = {
#            "id" : e.employeeid,
#            "nombre" : e.firstname,
#            "apellido" : e.lastname,
#            "birthdate" : e.birthdate
#        }
#        if e.birthdate.year >= int(year):
#            resultados.append(resultado)
#    serializados = Punto1Serializer(resultados, many=True)
#    return Response(serializados.data)   

class ProductoSerializer(serializers.Serializer):
   ProductId = serializers.IntegerField()
   ProductName = serializers.CharField()
   StockFuturo = serializers.CharField()