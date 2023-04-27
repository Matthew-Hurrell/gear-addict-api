from django.urls import path
from fans import views


urlpatterns = [
    path('fans/', views.FanList.as_view()),
    path('fans/<int:pk>/', views.FanDetail.as_view()),
]
