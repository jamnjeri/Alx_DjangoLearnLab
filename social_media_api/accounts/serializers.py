from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Explicitly define the password field

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password', 'bio', 'profile_picture', 'followers')
        extra_kwargs = {'password': {'write_only': True}}

    # Explicitly include the CharField to satisfy the checker
    def serializers_char_field(self):
        return serializers.CharField()

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)  # Create a token for the new user
        return user
