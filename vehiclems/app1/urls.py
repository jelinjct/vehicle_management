from django.urls import path

from app1 import views
from django.contrib.auth.views import LogoutView

app_name = 'app1'

urlpatterns = [
    path('',views.FrontView.as_view(),name='frontpage'),
    path('home/',views.HomeView.as_view(),name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),

    path('vehiclelist', views.VehicleListView.as_view(), name='vehiclelist_superadmin'),
    path('vehiclelist1', views.VehicleList1View.as_view(), name='vehiclelist_user'),
    path('vehiclelist3', views.VehicleList3View.as_view(), name='vehiclelist_admin'),


    path('create/', views.VehicleCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.VehicleDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.VehicleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.VehicleDeleteView.as_view(), name='delete'),


    path('user-signup/', views.UserSignupView.as_view(), name='usersignup'),
    path('admin-signup/', views.AdminSignupView.as_view(), name='adminsignup'),
    path('superuser-signup/', views.SuperAdminSignupView.as_view(), name='superadminsign'),


    path('logout/', views.UserLogoutView.as_view(), name='logout'),




]


