from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login,  get_user_model
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

from .forms import UserCustomCreationForm

# Create your views here.
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')


def accounts(request):
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/list.html', context)

def profile(request, user_pk):
    profile_user = get_object_or_404(get_user_model(), pk=user_pk)
    movie, temp = '', 0
    for follower in profile_user.followers.all():
        movie = follower.scored_movie.order_by('-pk').first()
    context = {
        'profile_user': profile_user,
        'recommand': movie,
    }
    return render(request, 'accounts/profile.html', context)
    
@login_required
def follow(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user in user.followers.all():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect('accounts:profile', user_pk)