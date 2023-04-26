from django.urls import path
from gear import views

urlpatterns = [
    path('gear/', views.GearList.as_view()),
    path('gear/<int:pk>/', views.GearDetail.as_view())
]
