from django.urls import path

from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("volonteur/", views.volonteur, name="volonteur"),
    path("victims/", views.victims, name="victims"),
    path("requests/<int:request_id>/", views.requests, name="request"),
    path('register/', views.register, name='register'),
    path('addprop/', views.add_proposition, name='addprop'),
    path('addreq/', views.add_req, name='addreq')
]