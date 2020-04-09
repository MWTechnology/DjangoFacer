from django.contrib.auth import views
from django.urls import path, include
from django.conf.urls import url
from . import views as s
from account.views import (
    PasswordResetTokenView,
    PasswordResetView,
)

urlpatterns = [
    path('login/', s.MyLoginView.as_view(), name='login'),

    path('login/', s.MyLogoutView.as_view(), name='logout'),

    path('password-change/', s.MyPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('register/', s.MyRegisterFormView.as_view(), name="register"),

    path('password-reset/', s.MyPasswordResetView.as_view(), name="account_password_reset"),
    path('reset/<uidb36>/<token>/', PasswordResetTokenView.as_view(), name='account_password_reset_token'),





    path ('someview/', s.someview, name='someview'),

]

