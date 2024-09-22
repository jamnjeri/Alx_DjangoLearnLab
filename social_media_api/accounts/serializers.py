from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Explicitly define the password field

    class Meta:
        model = get_user_model()  # Use the custom user model
        fields = ['id', 'username', 'password', 'bio', 'profile_picture']
        # password field is already set to write_only=True above

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
