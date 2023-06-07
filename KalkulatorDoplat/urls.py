"""
URL configuration for KalkulatorDoplat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, PasswordChangeDoneView, PasswordResetDoneView, PasswordResetConfirmView
from django.contrib.auth import views as auth_views

from Kalkulator.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wyloguj/', LogoutView.as_view(template_name='user/logout.html'), name='wyloguj'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('', main_page, name='main_page'),
    path('user/', include('user.urls')),
    path('platnosci', platnosci, name='platnosci'),
    path('podsumowanie', podsumowanie, name='podsumowanie'),
    path('oblicz', oblicz, name='oblicz'),
    path('podsumowanieplatnosci', podsumowanieplatnosci, name='podsumowanieplatnosci'),
    path('wyczysc', wyczysc, name='wyczysc'),
    path('platnoscjpo/<id>', platnoscjpo, name='platnoscjpo'),
    path('dodajwartoscjpo/<id>', dodajwartoscjpo, name='dodajwartoscjpo'),
    path('platnoscupp/<id>', platnoscupp, name='platnoscupp'),
    path('dodajwartoscupp/<id>', dodajwartoscupp, name='dodajwartoscupp'),
    path('platnoscp_str/<id>', platnoscp_str, name='platnoscp_str'),
    path('dodajwartoscp_str/<id>', dodajwartoscp_str, name='dodajwartoscp_str'),
    path('platnoscp_pas/<id>', platnoscp_pas, name='platnoscp_pas'),
    path('dodajwartoscp_pas/<id>', dodajwartoscp_pas, name='dodajwartoscp_pas'),
    path('platnoscp_burak/<id>', platnoscp_burak, name='platnoscp_burak'),
    path('dodajwartoscp_burak/<id>', dodajwartoscp_burak, name='dodajwartoscp_burak'),
    path('platnoscp_skrobia/<id>', platnoscp_skrobia, name='platnoscp_skrobia'),
    path('dodajwartoscp_skrobia/<id>', dodajwartoscp_skrobia, name='dodajwartoscp_skrobia'),
    path('platnoscp_trus/<id>', platnoscp_trus, name='platnoscp_trus'),
    path('dodajwartoscp_trus/<id>', dodajwartoscp_trus, name='dodajwartoscp_trus'),
    path('platnoscpomidor/<id>', platnoscpomidor, name='platnoscpomidor'),
    path('dodajwartoscpomidor/<id>', dodajwartoscpomidor, name='dodajwartoscpomidor'),
    path('platnoscchmiel/<id>', platnoscchmiel, name='platnoscchmiel'),
    path('dodajwartoscchmiel/<id>', dodajwartoscchmiel, name='dodajwartoscchmiel'),
    path('platnosclen/<id>', platnosclen, name='platnosclen'),
    path('dodajwartosclen/<id>', dodajwartosclen, name='dodajwartosclen'),
    path('platnosckonopie/<id>', platnosckonopie, name='platnosckonopie'),
    path('dodajwartosckonopie/<id>', dodajwartosckonopie, name='dodajwartosckonopie'),
    path('platnosctyton/<id>', platnosctyton, name='platnosctytone'),
    path('dodajwartosctyton/<id>', dodajwartosctyton, name='dodajwartosctyton'),
    path('platnoscvirginia/<id>', platnoscvirginia, name='platnoscvirginia'),
    path('dodajwartoscvirginia/<id>', dodajwartoscvirginia, name='dodajwartoscvirginia'),
    path('platnosckrowy/<id>', platnosckrowy, name='platnosckrowy'),
    path('dodajwartosckrowy/<id>', dodajwartosckrowy, name='dodajwartosckrowy'),
    path('platnoscbydlo/<id>', platnoscbydlo, name='platnoscbydlo'),
    path('dodajwartoscbydlo/<id>', dodajwartoscbydlo, name='dodajwartoscbydlo'),
    path('platnoscowce/<id>', platnoscowce, name='platnoscowce'),
    path('dodajwartoscowce/<id>', dodajwartoscowce, name='dodajwartoscowce'),
    path('platnosckozy/<id>', platnosckozy, name='platnosckozy'),
    path('dodajwartosckozy/<id>', dodajwartosckozy, name='dodajwartosckozy'),
    path('sankcjacc/<id>', sankcjacc, name='sankcjacc'),
    path('dodajwartosccc/<id>', dodajwartosccc, name='dodajwartosccc'),
    path('sankcjaefa/<id>', sankcjaefa, name='sankcjaefa'),
    path('dodajwartoscefa/<id>', dodajwartoscefa, name='dodajwartoscefa'),
    path('sankcjaniezad/<id>', sankcjaniezad, name='sankcjaniezad'),
    path('dodajwartoscniezad/<id>', dodajwartoscniezad, name='dodajwartoscniezad'),
    path('sankcjaterm/<id>', sankcjaterm, name='sankcjaterm'),
    path('dodajwartoscterm/<id>', dodajwartoscterm, name='dodajwartoscterm'),
    path('linki', linki, name='linki'),
]