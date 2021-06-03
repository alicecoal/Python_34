"""ZZShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from ZZShop import settings
from accounts import views
from accounts.views import home_view, signup_view, activation_sent_view, activate

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),  # админкая страничка
    path('', home_view, name="index"),  # index
    path('signup/', signup_view, name="signup"),  # страничка регистрации
    path('sent/', activation_sent_view, name="activation_sent"),  # отправка писем
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),  # активация писем при регистрации
    url(r'^account/', include('accounts.urls')),  # для аккаунтов
    path('shop/', include(('shop.urls', 'shop'), namespace="shop")),  # для магазинов
    path('wallet/', include('wallets.urls')),  # для кошельков
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),  # авторизация через соцсети
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # просмотр медиа файлов