from django.urls import path
from .views import CreateUser,UpdateUser,DeleteUser,UserList

urlpatterns=[
    path('',UserList,name='UserList'),
    path('create',CreateUser,name='CreateUser'),
    path('update/<int:id>',UpdateUser,name='UpdateUser'),
    path('delete/<int:id>',DeleteUser,name='DeleteUser'),

]