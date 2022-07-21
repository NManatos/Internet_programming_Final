from . import views
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index2, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_form, name='login'),
    path('booking/', views.booking, name='booking'),
    path('logout/', views.logout_form, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('ratings/', include('star_ratings.urls', namespace='ratings'))
]
urlpatterns += staticfiles_urlpatterns()

