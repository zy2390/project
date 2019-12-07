from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import Squirrel
from .forms import SquirrelForm #Build a Form

def index(request):
	return HttpResponse(b'sightings views index')

def all_sqrs(request):
	squirrels = Squirrel.objects.all()
	context={
		'squirrels':squirrels,
	}
	return render(request, 'sightings/all.html', context)

def sqr_coordinate(request, sqr_id):
	sqr = Squirrel.objects.get(Unique_Squirrel_ID=sqr_id)
	return HttpResponse(f'{sqr.Latitude,sqr.Longitude}')

def edit_sqr(request, sqr_id):
	sqr = Squirrel.objects.get(Unique_Squirrel_ID=sqr_id)
	if request.method =='POST':
		form = SquirrelForm(request.POST, instance=sqr)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/{sqr_id}')
	else:
		form = SquirrelForm(instance=sqr)

	context={
		'form':form,
	}
	return render(request, 'sightings/edit.html',context)

def add_pet(request):
	if request.method == 'POST':
		form = SquirrelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(f'/sightings/list')
	else:
		form = SquirrelForm

	context={
		'form':form,
	}
	return render(request, 'sightings/edit.html', context)