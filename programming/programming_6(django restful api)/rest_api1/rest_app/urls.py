from .views import ContainerView, ContainerIDView
from django.urls import path

urlpatterns = [
    path('containers/', ContainerView.as_view()),
    path('containers/<str:id>/', ContainerIDView.as_view()),
]