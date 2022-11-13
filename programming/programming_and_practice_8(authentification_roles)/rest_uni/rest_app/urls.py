from .views import ContainerIDView, ContainerListCreateApiView
from .container_order_views import ContainerOrderViewSet
from .authentification_views import RegisterView, LogoutUserView
from django.urls import path
from .swagger.swagger import url_patterns as swagger_urls
from .authentification_views import LoginTokenObtainPairView, LoginRefreshTokenView
urlpatterns = [
    path('containers/', ContainerListCreateApiView.as_view()),
    path('containers/<str:id>/', ContainerIDView.as_view()),
    path('login/', LoginTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', LoginRefreshTokenView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('logout/', LogoutUserView.as_view(), name='auth_logout'),
    path('orders/', ContainerOrderViewSet.as_view({"get": "list", "post": "create"})),
    path('orders/<str:pk>/', ContainerOrderViewSet.as_view({"get": "retrieve"})),
    #although django has some automatic settings and redirects urls without slash to paths with slash
    #(in case it`s not found), POST and PUT request are not working properly that way, bacause
    #data is lost on the way
    #so I decided to put it here, hope it`s a good practice
    #path('containers', ContainerView.as_view()),
    #path('containers/<str:id>', ContainerIDView.as_view()),
]


urlpatterns += swagger_urls

