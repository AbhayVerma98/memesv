from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('videos/', views.Videos, name='videos'),
    path('home/', views.Home, name='home'),
    path('aboutus/', views.Aboutus, name='aboutus'),
    path('templates/', views.Temp, name='templates'),
    path('master/', views.Search, name='master'),
    # path('/',views.,name=''),
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('profile/', views.Profile, name='profile'),
    path('updateprofile/', views.UpdateProfile, name='updateprofile'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html',
                                                                   success_url='/YFI/change_password/'),
         name='change_password'),
    # path('change_password',views.change_password,name='change pssword'),
    # Forget Password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    path('celebrity/', views.Celebrity, name='celebrity'),
    path('webserise/', views.Web_series, name='web_serise'),
    path('anime/', views.Anime, name='anime'),
    path('random/', views.Random, name='random'),
    path('new/', views.New, name='new'),
    path('all/', views.All, name='all'),
    path('cartoon/', views.Cartoon, name='cartoon'),
    path('popular/', views.Popular, name='popular'),

    path('v_celebrity/', views.v_Celebrity, name='v_celebrity'),
    path('v_webserise/', views.v_Web_series, name='v_web_serise'),
    path('v_abusive/', views.v_Abusive, name='v_abusive'),
    path('v_random/', views.v_Random, name='v_random'),
    path('v_new/', views.v_New, name='v_new'),
    path('v_all/', views.v_All, name='v_all'),
    path('v_funny/', views.v_Funny, name='v_funny'),
    path('v_popular/', views.v_Popular, name='v_popular'),
]
