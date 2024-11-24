from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from UserApp.models import Users

class userSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)

    class Meta:
        model=Users
        fields= ['_id', 'name', 'password', 'email', 'profile', 'created_at', 'updated_at']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['name'] = user.name
        return token