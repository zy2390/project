from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:sqr_id>',views.update),
    path('add',views.add),
]
