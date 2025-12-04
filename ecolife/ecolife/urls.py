from django.contrib import admin
from django.urls import include, path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('carbon/', include('eco.urls')), 
    path("electricity/", include("electricity.urls")),
    path('history/', include('history.urls')),
    path('', include('accounts.urls')),
    

]

