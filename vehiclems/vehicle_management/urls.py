from django.urls import path
from vehicle_management import views

app_name='vehicle_management'

urlpatterns=[
    path('',views.VehicleManagementLoginView.as_view(), name='login'),
    path('vehicle/',views.VehicleListView.as_view(),name='list'),
    path('create/', views.VehicleCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.VehicleDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.VehicleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.VehicleDeleteView.as_view(), name='delete'),
    ]


