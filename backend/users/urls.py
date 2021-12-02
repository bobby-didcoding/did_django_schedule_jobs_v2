
from django.urls import path
from . import views
 
app_name = "users"
 
urlpatterns = [
    path('', views.SignUpView.as_view(), name="home"),
    path('sign-in/', views.SignInView.as_view(), name="sign-in"),
    path('sign-out/', views.sign_out, name="sign-out"),
    path('account/', views.AccountView.as_view(), name="account"),
    ]
 
