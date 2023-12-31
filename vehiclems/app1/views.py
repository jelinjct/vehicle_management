
from django.views import View
from app1.forms import CustomUserCreationForm

from django.contrib.auth.views import LogoutView
from app1.models import User1,Vehicle,UserAccess
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView ,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin



from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm



class FrontView(TemplateView):
    template_name = 'front_webpage.html'
class HomeView(TemplateView):
    template_name = 'home.html'

# to see list of vehicles for Super admin
class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'list-view_owner.html'
    context_object_name = 'vehicles'
    login_url = '/login/'

# to see list of vehicles for User(has view option)
class VehicleList1View(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'list_view_user.html'
    context_object_name = 'vehicles'
    login_url = '/login/'
#to see list of vehicles for admin
class VehicleList3View(LoginRequiredMixin, ListView):
    model = Vehicle
    template_name = 'list_view_staff.html'
    context_object_name = 'vehicles'
    login_url = '/login/'

# view to display details
class VehicleDetailView(LoginRequiredMixin, DetailView):
    model = Vehicle
    template_name = 'detail.html'
    context_object_name = 'vehicle'
    login_url = '/login/'

    def get_success_url(self):
        return reverse_lazy('app1:detail', kwargs={'pk': self.object.pk})


# view to create vehicle
class VehicleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vehicle
    template_name = 'create.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('app1:home')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type in ['Super admin']
    def form_valid(self, form):
        # Set the current user as the owner of the vehicle being created
        form.instance.vehicle = self.request.user
        return super().form_valid(form)


# view to update vehicle
class VehicleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vehicle
    template_name = 'update.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('app1:home')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'

    def test_func(self):
        return self.request.user.user_type in ['Super admin', 'Admin']

    def get_success_url(self):
        return reverse_lazy('app1:home')

# view to delete vehicle
class VehicleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vehicle
    template_name = 'delete.html'
    success_url = reverse_lazy('app1:home')
    login_url = '/login/'
    permission_denied_message = 'Unauthorized Access'
    def test_func(self):
        return self.request.user.user_type in ['Super admin']


# view to user login

class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)


        if user:
            if user.user_type == 'User':
                    login(self.request, user)
                    list1_url = reverse('app1:home')
                    return redirect(list1_url)  # Redirect to Vehiclelist1View
            elif user.user_type == 'Admin':
                    login(self.request, user)
                    list_url = reverse('app1:home')
                    return redirect(list_url)  # Redirect to VehicleList3View
            elif user.user_type == 'Super admin':
                    login(self.request, user)
                    create_url = reverse('app1:home')
                    return redirect(create_url)  # Redirect to VehicleCreateView

        return HttpResponse("Invalid login details.....")



#view to signup for user
class UserSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'user_signup.html'
    success_url = reverse_lazy('app1:frontpage')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 'User'  # Set the user_type to 'User'
        user.save()
        return super().form_valid(form)

#signup for superadmin
class SuperAdminSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'superadmin_signup.html'
    success_url = reverse_lazy('app1:frontpage')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 'Super admin'  # Set the user_type to 'Super admin'
        user.save()
        return super().form_valid(form)

#signup for admin
class AdminSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'adminsignup.html'
    success_url = reverse_lazy('app1:frontpage')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.user_type = 'Admin'  # Set the user_type to 'Admin'
        user.save()
        return super().form_valid(form)



# view for logout
class UserLogoutView(LogoutView):
    def get(self, request):
        logout(request)
        logout_url = reverse('app1:frontpage')
        return redirect(logout_url)


