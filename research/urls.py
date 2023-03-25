from django.urls import path

from . import views

app_name = 'research'
urlpatterns = [
    # ex: /research/
    path('', views.index, name='index'),

    # ex: /research/reference
    path('/reference', views.reference.handleRequest, name='create-reference'),
    # ex: /research/reference/1234567890
    path('/reference/<uuid:reference_id>', views.reference.handleRequest, name='update-reference'),

    # ex: /research/resource?reference_id=1
    path('/reference', views.resource.handleRequest, name='create-resource'),
    # ex: /research/resource/1234567890
    path('/reference/<uuid:resource_id>', views.resource.handleRequest, name='update-resource'),
]