from rest_framework import serializers
from .models import User, Customer, SwiftConnection

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'user_type']
        
    def create(self, validated_data):
        password = validated_data.pop("password")
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def get(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
        


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'email', 'password']
        read_only_fields = ['id']

class SwiftConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiftConnection
        fields = ['id', 'companyName', 'companyAddress', 'contactPhone', 'contactEmail', 'status' ]
        read_only_fields = ['id']