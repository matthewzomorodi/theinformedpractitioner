from django.urls import path

from . import views

app_name = 'research'
urlpatterns = [
    # ex: /theinformedpractitioner/research
    path('', views.index, name='index'),
]