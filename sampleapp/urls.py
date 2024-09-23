from django.urls import path
from . import views
from .views import signup_view, dashboard_view
from django.contrib.auth import views as auth_views

# urlpatterns = [
#     path('login/', login_view, name='login'),
#     path('signup/', signup_view, name='signup'),
#     path('dashboard/',dashboard_view,name='dashboard'),
# ]    

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
