from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomUserChangeForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('signup')
    template_name = 'registration/signup.html'

class ProfileView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile.html'

    def get_object(self):
        return self.request.user

def home(request):
    return render(request, 'home.html')