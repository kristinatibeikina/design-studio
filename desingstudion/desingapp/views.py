from django.shortcuts import render
from .forms import Registration
from .forms import LoginForm
from django.shortcuts import redirect
from .models import User, Application
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def base(request):
    return render(request, "base.html",)


def cabinet(request):
    return render(request, "cabinet.html",)


def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email,password)
            user.first_name = full_name
            user.save()
            dj_login(request, user)
            return redirect('login')
    else:
        form = Registration()

    return render(request, 'registration/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                dj_login(request, user)
                return redirect('cabinet')
            else:
                form.add_error(None, 'Неверный логин или пароль')
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})


class ApplicationListView(generic.ListView):
    model = Application
    paginate_by = 4
    template_name = 'base.html'


def logout(request):
    return render(request, "logout.html",)


class ApplicationCreate(CreateView):
    model = Application
    fields = ['name', 'description', 'category', 'photo_file']
    template_name = 'main_request.html'


def requestmain(request):
    return render(request, "main_request.html",)



