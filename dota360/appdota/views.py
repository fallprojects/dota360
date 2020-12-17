from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import *
from .models import *
from django_filters import OrderingFilter
from .filters import heroFilter
# Create your views here.

def heroList(request):
    heroes = Hero.objects.all()
    filter = heroFilter(request.GET, queryset=heroes)
    heroes = filter.qs
    context = {'heroes': heroes, 'filter': filter}
    return render(request, 'heroes.html', context)
