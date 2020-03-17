from django.urls import path, re_path, reverse_lazy
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'


urlpatterns = [

    # Login / Logout URLs
    re_path(r'^login/$', views.accounts_login, name="accountLogin"),
    re_path(r'^logout/$', views.accounts_logout, name="accountLogout"),
    re_path(r'^signup/$', views.account_create, name="accountSignup"),
    re_path(r'^myprofile/$', views.user_profile, name="profile"),


    re_path(r'^password/$', views.change_password, name='change_password'),
    # PASSWORD  CHANGE ROUTE
    path('password_change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('accounts:password_change_done'),
                                                                   template_name='registration/password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'), name='password_change_done'),
    # PASSWORD RESET
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('accounts:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    re_path(r'confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('accounts:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),


]
