from django.urls import path
from .views import SignUpView, ProfileView,  home
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
