"""
URL configuration for catalystproject project.

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
from django.urls import path,include
from crm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('explorer/', include('explorer.urls')),
    # Configured the URL
    path('', views.index, name="login_page"),
    path('login/', views.login_api, name='login_api'),
    path('home/', views.home, name='home_page'),
    path('add_user/', views.user_registration, name='add_user'),
    path('upload-chunk/', views.upload_chunk, name='upload-chunk'),
    path('logout/', views.LogoutPageView.as_view(), name='logout'),
    # path('user_list/', views.GetUsers.as_view(), name='user_list'),
    path('user_list/', views.get_users, name='user_list'),
    path('query_build/', views.QueryBuilder.as_view(), name='query_build'),
    path('upload/', views.Upload.as_view(), name='upload')
    # path('query_builder',views.QueryBuilder.as_view(),name='query_build'),
    # Bulk Upload
    

]
