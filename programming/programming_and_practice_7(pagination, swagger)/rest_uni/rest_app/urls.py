from .views import ContainerView, ContainerIDView
from django.urls import path
from .swagger import url_patterns as swagger_urls

urlpatterns = [
    path('containers/', ContainerView.as_view()),
    path('containers/<str:id>/', ContainerIDView.as_view()),
    #although django has some automatic settings and redirects urls without slash to paths with slash
    #(in case it`s not found), POST and PUT request are not working properly that way, bacause
    #data is lost on the way
    #so I decided to put it here, hope it`s a good practice
    #path('containers', ContainerView.as_view()),
    #path('containers/<str:id>', ContainerIDView.as_view()),
]


urlpatterns += swagger_urls

