from rest_framework import generics, permissions,views
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializer import RegisterSerializer,LoginSerializer,UserSerializer
from knox.models import AuthToken
from knox.auth import TokenAuthentication

class RegistrationAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer


    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response({
            "user": RegisterSerializer(user, context = self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer


    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data
        _,token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context = self.get_serializer_context()).data,
            "token": token
        })


class GetUser(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication,]
    # permission_classes = [
    #     permissions.IsAuthenticated,
    #     ]
    queryset = User.objects.all()