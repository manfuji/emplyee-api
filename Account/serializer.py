from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from Record.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email","password")
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username","email","password")
        extra_kwargs = {"password":{"write_only":True},}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data["username"],validated_data["email"],
        validated_data["password"])
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("invalid credentials")    


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ['prouser']
        depth =1

    def validate(self,attrs):
        attrs['prouser'] = self.context['request'].user
        return attrs

    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['prouser'] = UserSerializer(instance.prouser).data
        return response


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
