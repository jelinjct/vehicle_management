
from django.urls import reverse
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

from django.shortcuts import render
from user_access.models import Vehicle
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'

# to see list of vehicles
class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'list.html'
    context_object_name = 'vehicles'
    login_url = '/login/'

# view to display details
class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'detail.html'
    context_object_name = 'vehicle'
    login_url = '/login/'

# view to create vehicle
class VehicleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vehicle
    template_name = 'create.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('vehicle_management:list')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type in ['Super admin', 'Admin']

# view to update vehicle
class VehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vehicle
    template_name = 'vehicle_management/update.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('vehicle_management:list')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type in ['Super admin', 'Admin']

# view to delete vehicle
class VehicleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle_management/delete.html'
    success_url = reverse_lazy('vehicle_management:list')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type == 'Super admin'

# view to user login
class UserLoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_user:
                login(request, user)
                vehicle_list_url = reverse('vehiclelist')
                detail_url = reverse('detail')
                return redirect(vehicle_list_url)  # Redirect to VehicleListView
            elif user.is_admin:
                login(request, user)
                update_url = reverse('update')    # Generate URL for VehicleUpdateView
                return redirect(update_url)  # Redirect to VehicleUpdateView
            elif user.is_superadmin:
                login(request, user)
                create_url = reverse('create')  # Generate URL for VehicleCreateView
                return redirect(create_url)  # Redirect to VehicleCreateView
        return HttpResponse("Invalid login details.....")


#view to signup for user
class UserSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user_signup.html'
    success_url = reverse_lazy('user_access:home')

    def form_valid(self, form):
        form.instance.is_user = True
        return super().form_valid(form)

#signup for superadmin
class SuperAdminSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'superadmin_signup.html'
    success_url = reverse_lazy('user_access:home')

    def form_valid(self, form):
        form.instance.is_superadmin = True
        return super().form_valid(form)

#signup for admin
class AdminSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'adminsignup.html'
    success_url = reverse_lazy('user_access:home')

    def form_valid(self, form):
        form.instance.is_admin = True
        return super().form_valid(form)



#view for logout
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(HomeView.as_view())
