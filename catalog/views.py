from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View

# Create your views here.


class Home(View):
    def get(self, request, *args):
        return render(request, 'home.html')


def signup(request):


