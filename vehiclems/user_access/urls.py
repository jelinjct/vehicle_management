from django.urls import path
from user_access.views import UserProfileView

app_name = 'user_access'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
]
