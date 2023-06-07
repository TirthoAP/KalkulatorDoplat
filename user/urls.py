#””Definiuje wzorce adresów URL dla aplikacji users.”””
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.urls import reverse_lazy
from . import views


app_name='user'
urlpatterns = [
    # Dołączenie domyślnych adresów URL uwierzytelniania.
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('password_change/',
        auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('user:password_change_done')),
        name='password_change'),
    path('password_change/done/',
        auth_views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    path('password_reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    path('reset/done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
    ]