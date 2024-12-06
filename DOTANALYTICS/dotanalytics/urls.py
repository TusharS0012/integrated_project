"""
URL configuration for dotanalytics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
     
    path('signup/',views. RegisterView.as_view(), name='signup'),
    path('login/',views. LoginView.as_view(), name='login'),
    path('',views.home, name='home '),
    path('saas/', views.saas_view, name='saas'),
    path('MachineLearning/', views.MachineLearning_view, name='MachineLearning'),
    path('ArtficialIntelligence/', views.ArtficialIntelligence_view, name='ArtficialIntelligence'),
    path('python/', views.python_view, name='python'),
    path('cyber/', views.cyber_view, name='cyber'),
    path('docker/', views.docker_view, name='docker'),
    path("request_otp/", views.RequestOTPView.as_view(), name="request_otp"),
    path("validate_and_reset/", views.ValidateOTPAndResetPasswordView.as_view(), name="validate_and_reset"),

]