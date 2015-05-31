from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'base/homepage.html', {})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            url = reverse('profile', args=(), kwargs={'user_id': user.id})
            return HttpResponseRedirect(url)
        else:
            return render(request, 'registration/login.html', {'form': form})

    if request.method == "GET":
        form = AuthenticationForm()
        context = {'form': form, 'abc': request.user}
        return render(request, 'registration/login.html', context)


def logout_view(request):
    logout(request)
    # RE-DIRECT TO DEFAULT HOME PAGE
    url = reverse('homepage', args=(), kwargs={})
    return HttpResponseRedirect(url)
