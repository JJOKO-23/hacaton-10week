from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import RegistrationForm


class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('home')
    # success_message = 'Successfully registered'


class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')


def profile(request):
    return render(request, 'account/profile.html')

