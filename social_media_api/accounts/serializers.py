from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}  # Make password write-only

    def create(self, validated_data):
        # Create a user instance
        user = get_user_model().objects.create_user(**validated_data)
        # Create a token for the user
        Token.objects.create(user=user)
        return user
