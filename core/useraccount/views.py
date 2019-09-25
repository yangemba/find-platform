from django.shortcuts import render

from django.utils import timezone
from django.views.generic import TemplateView, FormView, RedirectView, View, \
    ListView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views


# Create your views here.
class Login(auth_views.LoginView):

    template_name='login.html'

    def login(request, *args, **kwargs):
        # render(request, template_name="login.html")

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)