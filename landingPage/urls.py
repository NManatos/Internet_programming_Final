#import sqlite3
from landingPage import views
#from .viewsets import UserViewSet,EventViewSet
from django.urls import path, include
#from rest_framework import routers
#from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [
    path('', views.index2, name = 'index'),
    path('register/',views.register,name= 'register'),
    path('login/', views.login,name ='login'),
    path('booking/',views.booking,name ='booking'),
    path('logout/',views.logout,name ='logout'),
    path('profile/', views.profile,name ='profile'),
    path('ratings/', include('star_ratings.urls', namespace ='ratings'))
    ]


# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, basename=sqlite3)
# router.register(r'events', EventViewSet,basename=sqlite3)

# urlpatterns = [
#     path('router/', include(router.urls),name='router'),
#     path('create/',views.Event_Creator.as_view()),
#     path('api/', include('rest_framework.urls', namespace ='rest_framework')),
#    
# ]

#urlpatterns = format_suffix_patterns(urlpatterns)
