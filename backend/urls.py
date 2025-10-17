from django.urls import path,include
from . import views
from social_django.urls import urlpatterns as social_django_urls

urlpatterns=[
    path('login/',views.LoginAPIView.as_view(),name='login'),
    path('register/',views.RegistrationAPIView.as_view(),name='register'),
    path('register/token/count/',views.Token_Click.as_view(),name='register_token'),
    path('logout/',views.LogoutAPIView.as_view(),name='logout'),
    path('google/',views.SocialLoginView.as_view(),name='google'),
    path('google/complete/',views.SocialLoginComplete.as_view(),name='google_complete'),
    path('change_password/',views.Change_password.as_view(),name='change_password'),
    path('password_reset/',views.RequestPasswordReset.as_view(),name='reset_password'),
    path('password_reset/<str:token>/', views.PasswordResetConfirm.as_view(), name='reset-password-confirm'),
    path('profile/',views.Profile_View.as_view(),name='profile'),
    path('profile/balance',views.Profile_balance.as_view(),name='profile_balance'),
    path('profile/mainpage',views.GetMain.as_view(),name='profile_main'),
    path('profile/mainpage/chart_daily',views.GetMain_chart_daily.as_view(),name='main_chart_daily'),
    path('profile/mainpage/chart_weekly',views.GetMain_chart_weekly.as_view(),name='main_chart_weekly'),
    path('profile/mainpage/chart_monthly',views.GetMain_chart_monthly.as_view(),name='main_chart_monthly'),
    path('referal/link',views.GetRefral_link.as_view(),name='referal_link'),
    path('referal/list',views.Refer_list.as_view(),name='list'),
    path('referal/count/daily',views.Referall_count_daily.as_view(),name='ref_daily'),
    path('referal/count/weekly',views.Referall_count_weekly.as_view(),name='ref_weekly'),
    path('referal/count/monthly',views.Referall_count_monthly.as_view(),name='ref_monthly'),
    path('wallet/list',views.GetWallet.as_view(),name='wallet_list'),
    path('wallet/',views.GetWalletType.as_view(),name='wallet'),
    path('withdraw/',views.Withdraw_View.as_view(),name='withdraw'),
    path('level/list',views.PartnerLevelView.as_view(),name='level_list'),
    path('register/broker',views.RegisterBrokerView.as_view(),name='broker_register')


]
