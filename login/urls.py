from django.urls import path
from . import views

urlpatterns = [
      path('', views.user_login, name='login'),
      path ('signup/', views.sign_up, name='sign_up'),
 ]