from django.urls import path
from . import views

app_name = "webapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name = 'login'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('logout', views.user_logout, name = 'logout'),
    path('create-record', views.create_record, name = 'create-record'),
    path('update-record/<int:pk>', views.update_record, name = 'update-record'),
    path('record/<int:pk>', views.view_record, name='record'),
    path('delete-record/<int:pk>', views.delete_record, name= 'delete-record'),
]
