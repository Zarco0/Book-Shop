from django.urls import path
from .import views

app_name = 'webaccount'

urlpatterns = [
    path('',views.UserRegistration,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/',views.logout_view,name='logout')

    
]