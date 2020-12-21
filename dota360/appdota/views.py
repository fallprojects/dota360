from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
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


def heroInfo(request,hero_name):
        try:
            hero = Hero.objects.get(name=hero_name)
        except Hero.DoesNotExist:
            return HttpResponse('Theres no such hero.404')
        context = {'hero': hero}
        return render(request, 'hero-info.html', context)



def guideCreate(request):
    form = GuideForm()
    if request.method == 'POST':
        form = GuideForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'guide_form': form}
    return render(request, 'guide-create.html', context)


def guideList(request):
    guides = Guide.objects.all()
    context = {'guides': guides}
    return render(request,'guide-list.html',context)

def guideView(request,hero_name):
    try:
        guide = Guide.objects.get(hero__name=hero_name)
    except Hero.DoesNotExist:
        return HttpResponse('Theres no such hero.404')
    context = {'guide': guide}
    return render(request, 'guide-view.html', context)


