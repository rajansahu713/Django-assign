from django.urls import path
from .views import ProfileView

urlpatterns = [
    path('user_profile/', ProfileView.as_view(), name="userprofile")
    
]