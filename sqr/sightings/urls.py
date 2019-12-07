from django.urls import path
from . import views

app_name = 'sightings'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.all_sqrs),
    path('sqr_id',views.sqr_coordinate),
    path('sqr_id/edit',views.edit_sqr),
]
