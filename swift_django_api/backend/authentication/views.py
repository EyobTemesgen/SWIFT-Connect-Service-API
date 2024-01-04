from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User, Customer, SwiftConnection
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken, TokenError
from rest_framework import status
from .serializers import  CustomerSerializer, SwiftConnectionSerializer
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import Group, Permission

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        user = User.objects.get(id=id)
        user.delete()
        return Response("User Deleted Successfully")

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    

class Loginview(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        print("Received from React", email, password)
        
        try:
            user = User.objects.get(email = email)
        except User.DoesNotExist:
            raise AuthenticationFailed("Account does  not exist")

        if user is None:
            raise AuthenticationFailed("User does not exist")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect Password")
        access_token = str(AccessToken.for_user(user))
        refresh_token = str(RefreshToken.for_user(user))
        return Response({
            "access_token" : access_token,
            "refresh_token" : refresh_token
        })
    
class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response("Logout Successful", status=status.HTTP_200_OK)
        except TokenError:
            raise AuthenticationFailed("Invalid Token")



class CustomerView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        customer = Customer.objects.get(id=pk)
        customer.delete()
        return Response("Customer Deleted Successfully")



class SwiftConnectionView(APIView):
    def get(self, request):
        connections = SwiftConnection.objects.all()
        serializer = SwiftConnectionSerializer(connections, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SwiftConnectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Connection Created Successfully")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)