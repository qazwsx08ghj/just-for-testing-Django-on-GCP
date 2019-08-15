"""QAQ2016712_site URL Configuration

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
from django.urls import path
from site_app.views import index
from chatroom_stuff.views import chat,room
from django.conf.urls import include



urlpatterns = [
    path('', index),
    path('chat-room-select/',include('chatroom_stuff.urls'),name = 'chat-rooms'),
    path('admin/', admin.site.urls),
]
