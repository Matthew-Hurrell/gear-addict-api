from django.urls import path
from rigs import views


urlpatterns = [
    path('rigs/', views.RigList.as_view()), 
]
