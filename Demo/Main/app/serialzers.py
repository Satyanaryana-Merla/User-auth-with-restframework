from rest_framework import serializers
from django.contrib.auth.models import User
# from tomlkit import value


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serlizer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, Validated_data):
        user = User.objects.create_user(Validated_data['username'], Validated_data['email'], Validated_data['password'])    # type: ignore
        return user
