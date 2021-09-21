from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Employee,Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = ("id","name","description","price","category","available")

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = ("name","owner","description","price","category")

class MakeSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = ("owner","product","quantity","price","total_price")

class FetchSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = ("owner","product","quantity","price","total_price","Published")
                
    

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id","owner","product","quantity","price")

        
class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username")