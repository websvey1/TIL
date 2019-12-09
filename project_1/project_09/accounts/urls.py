from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('follow/<int:user_pk>/', views.follow, name='follow'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/', views.profile, name='profile'),
    path('', views.accounts, name='accounts'),
    ]