from django.urls import path
from . import views


urlpatterns=[path('',views.home,name='home'),
             #path('login/',views.login_user,name='login'),
             path('logout/',views.logout_user,name='logout'),
             path('register/',views.register_user,name='register'),
             path('details/<int:key>/',views.details,name='details'),
             path('delete_record/<int:key>/',views.delete_record,name='delete_record'),
             path('add_record/',views.add_record,name='add_record'),
             path('update_record/<int:key>/',views.update_record,name='update_record')]