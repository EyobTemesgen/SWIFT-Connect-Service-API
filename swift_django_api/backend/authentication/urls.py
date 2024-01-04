from django.contrib import admin
from django.urls import path, include
from .views import Loginview, RegisterView, LogoutView, SwiftConnectionView

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', Loginview.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name = "logout"),
    path('swift', SwiftConnectionView.as_view(), name="swift-connection"),
]
