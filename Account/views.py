from rest_framework import viewsets,generics,views
from django.contrib.auth.models import User
from .serializer import UserSerializer,ProfileSerializers,ChangePasswordSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Record.models import Profile
from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication,]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(username=user)

class ChangePasswordView(generics.UpdateAPIView):
        """
        An endpoint for changing password.
        """
        serializer_class = ChangePasswordSerializer
        model = User
        authentication_classes = [TokenAuthentication,]

        # permission_classes = (IsAuthenticated,)

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def update(self, request, *args, **kwargs):
            print(request.data) 
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(views.APIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    def get(self,request):
        print(request.user)
        try:
            query = Profile.objects.get(prouser=request.user)
            serializer = ProfileSerializers(query)
            response_message = {"error":False,"data":serializer.data}
        except:
            response_message = {"error":True,"message":"Somthing is Wrong"}
        return Response(response_message)


class Updateprofile(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication,]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ProfileSerializers
    queryset = Profile.objects.all()


 
         
              