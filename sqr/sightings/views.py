from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import Squirrel
from .forms import SquirrelForm #Build a Form

def index(request):
	sightings = Squirrel.objects.all()
	context={'sightings':sightings}
	return render(request, 'sightings/index.html',context)

# def all_sqrs(request):
# 	squirrels = Squirrel.objects.all()
# 	context={
# 		'squirrels':squirrels,
# 	}
# 	return render(request, 'sightings/all.html', context)

# def sqr_coordinate(request, sqr_id):
# 	sqr = Squirrel.objects.get(Unique_Squirrel_ID=sqr_id)
# 	return HttpResponse(f'{sqr.Latitude,sqr.Longitude}')

def update(request,sqr_id):
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
	return render(request, 'sightings/update.html',context)

def add(request):
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
	return render(request, 'sightings/add.html', context)