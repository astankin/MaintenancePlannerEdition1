from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView

from MaintenancePlanner.accounts.decorators import unauthenticated_user, allowed_users
from MaintenancePlanner.accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from MaintenancePlanner.accounts.mixins import AllowedUsersMixin
from MaintenancePlanner.accounts.models import AppUser


@login_required
@allowed_users(allowed_roles=['MANAGER'])
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return render(request, 'success-register.html', {'username': username})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            return redirect('home-page')
        else:
            messages.warning(
                request,
                'Please enter a correct username and password. Note that both fields may be case-sensitive.',
            )
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


@login_required
def profile(request):
    return render(request, 'profile/profile.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account have been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile/profile-update.html', context)


class ListUsers(LoginRequiredMixin, AllowedUsersMixin, ListView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = AppUser
    template_name = 'users-list.html'
    context_object_name = 'users'


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = AppUser
    context_object_name = 'users'
    success_url = reverse_lazy('users-list')
