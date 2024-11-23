from rest_framework import serializers
from UserApp.models import Users

class userSerializer(serializers.ModelSerializer):
    _id = serializers.CharField(read_only=True)

    class Meta:
        model=Users
        fields= ['_id', 'name', 'password', 'email', 'profile', 'created_at', 'updated_at']

