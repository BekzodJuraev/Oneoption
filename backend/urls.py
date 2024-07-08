from django.urls import path,include
from . import views
from social_django.urls import urlpatterns as social_django_urls

urlpatterns=[
    path('login/',views.LoginAPIView.as_view(),name='login'),
    path('register/',views.RegistrationAPIView.as_view(),name='register'),
    path('logout/',views.LogoutAPIView.as_view(),name='logout'),
    path('google/',views.SocialLoginView.as_view(),name='google'),
    path('change_password/',views.Change_password.as_view(),name='change_password'),
    path('password_reset/',views.RequestPasswordReset.as_view(),name='reset_password'),
    path('password_reset/<str:token>/', views.PasswordResetConfirm.as_view(), name='reset-password-confirm'),
    path('profile/',views.Profile_View.as_view(),name='profile'),
    path('referal/doxod',views.GetRefraldoxod.as_view(),name='doxod'),
    path('referal/oborot',views.GetRefraloborot.as_view(),name='oborot'),
    path('referal/sub',views.GetRefralsub.as_view(),name='sub'),
    path('referal/list',views.Refer_list.as_view(),name='list')

    #path('asd',views.google,name='asd')

]
