from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skillsA', views.skillsA, name='skillsA'),
    path('skillsB', views.skillsB, name='skillsB'),
    # path('skillsC', views.skillsC, name='skillsC'),

]
