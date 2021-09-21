from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Employee,Product
from .serializer import CreateProductSerializer, EmployeesSerializer, FetchSaleSerializer,MakeSaleSerializer, ProductSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework.views import APIView



class MakeSale(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = MakeSaleSerializer
    permisssion_classes = [
        IsAuthenticated,
    ] 

class Fetchsales(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('Published')
    serializer_class = FetchSaleSerializer
    permisssion_classes = [
        IsAuthenticated,
    ] 


class FetchSale(APIView):
    serializer_class = FetchSaleSerializer
    # permission_classes = (permissions.AllowAny,)
    
    def post(self,request,format= None,):
        data = self.request.data
        print(data)
        owner = data['owner']
        queryset = Employee.objects.order_by('Published').filter(owner__iexact=owner)

        serializer = FetchSaleSerializer(queryset,many = True)
        return Response(serializer.data)    
   
class CreateProduct(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

class Product(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer






    
 
        

