from django.shortcuts import render
from .forms import Registration
from .forms import LoginForm, ChangeStatusRequest
from django.shortcuts import redirect
from .models import User, Application,  Category
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.views import generic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



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
    template_name = 'base.html'
    context_object_name = 'application_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_application'] = Application.objects.filter(status__exact='Принято в работу').count()
        return context

    def get_queryset(self):
        return Application.objects.filter(status__exact='Выполнено').order_by('-date')[:4]




def logout(request):
    return render(request, "logout.html",)


class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    fields = ['name', 'description', 'category', 'photo_file']
    template_name = 'main_request.html'
    success_url = reverse_lazy('main_request')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def requestmain(request):
    return render(request, "main_request.html",)


class MyPostListViews(generic.ListView):
    model = Application
    context_object_name = 'posts'
    template_name = 'reguest_user.html'
    success_url = reverse_lazy('main_request')

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user).order_by('-date')



class ApplicationDelete(DeleteView):
    model = Application
    context_object_name = 'posts'
    template_name = 'application_confirm_delete.html'
    success_url = reverse_lazy('user_posts')








class ApplicationListViewAdmin(generic.ListView):
    model = Application
    template_name = 'base.html'
    context_object_name = 'application_list'

    def get_queryset(self):
        return Application.objects.order_by('-date')[:4]


class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category_list'

class CategoryDelete(DeleteView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category_list')


