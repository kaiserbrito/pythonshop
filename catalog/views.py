from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SignUpForm

# Create your views here.


class Home(View):
    def get(self, request, *args):
        return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


