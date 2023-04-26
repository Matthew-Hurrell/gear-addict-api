from django.urls import path
from gear import views

urlpatterns = [
    path('gear/', views.GearList.as_view()),
]
