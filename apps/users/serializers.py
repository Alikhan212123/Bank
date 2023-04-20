from rest_framework import serializers

from apps.users.models import User 



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, write_only=True
    )
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name', 
                  'last_name', 'email','password', 'password2')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password' : 'Пароли отличаются'})
        return attrs