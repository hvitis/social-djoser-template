"""social_djoser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from social_djoser.token import CustomJWTToken
from social_djoser.oauth.google import ObtainUserFromGoogle


urlpatterns = [
    # Original Admin panel
    path('admin/', admin.site.urls),
    path('api/auth/jwt/create', CustomJWTToken.as_view()),
    path('api/auth/', include('djoser.urls')),

    # URLs for Djoser/Django social OAuth2 login.
    path('api/auth/social/', include('djoser.social.urls')),
    path('api/auth/social_django/',
         include('social_django.urls', namespace='social')),
    path('accounts/profile/', ObtainUserFromGoogle.as_view()),
    path('api/auth/', include('djoser.urls.jwt')),

]
