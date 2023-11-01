from django.shortcuts import render
from .forms import Registration
from django.shortcuts import redirect
from .models import User
from django.contrib.auth import login


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
            user = User.objects.create_user(full_name, username, email, password)
            user.save()
            login(request, user)
            return redirect('cabinet')
    else:
        form = Registration()

    return render(request, 'registration/registration.html', {'form': form})