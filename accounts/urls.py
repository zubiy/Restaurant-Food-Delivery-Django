import django
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
import django.contrib.auth.views as v
app_name = 'accounts'

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change_password/', views.change_password, name='change_password'),

]
