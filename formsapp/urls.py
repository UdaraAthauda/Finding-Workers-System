from django.urls import path
from . import views

urlpatterns = [
    path('', views.base),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('userProfile', views.userProfile),
    path('changePassword', views.changePassword),
    path('workerDetail', views.addWorkerDetails),
    path('workerDetailDisplay/<int:param>/', views.workerDetailDisplay, name='workerDetailDisplay'),
    path('deleteMsg', views.deleteMsg),
    path('deleteUser', views.deleteUser),
    path('contactUs', views.contactUs),

]