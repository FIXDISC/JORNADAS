from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from API import views

urlpatterns = [
    url('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url('API/1.0/create_turno/', views.TurnosList.as_view()),
    url('API/1.0/elimina_turno/', views.TurnosList.as_view()),
    url('API/1.0/elimina_turno/(?P<pk>[0-9]+)/$', views.TurnosList.as_view()),
    url('API/1.0/turnos/(?P<pk>[0-9]+)/$', views.TurnosDetail.as_view())
]