from dataclasses import field, fields
from rest_framework import serializers

from .models import User


class user_serializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model =User

        fields=['email','name','password','password2']

        extra_kwargs={
            'password':{ 'write_only':True}
        }



    # validating {both password are same or not} 
    # Password and confirm password while registrations

    # attrs or data (same )

    def validate(self, attrs):
        password=attrs.get('password')

        password2=attrs.get('password2')

        if password!=password2:
            raise serializers.ValidationError('Password and Confirm Password does not match.')

        return attrs

    def create(self,validate_data):
        return User.objects.create_user(**validate_data)



class User_login(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User

        fields=('email','password')