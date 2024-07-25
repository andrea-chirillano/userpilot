from django.contrib import admin
from django.urls import path, include
from users.views import SignUpView, ProfileView,  home
from django.contrib.auth import views as auth_views 

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)