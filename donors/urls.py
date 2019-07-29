from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.redirec,name='redirect'),
    path('search',views.search,name='search'),
    path('record',views.record,name='record'),
    path('find',views.find,name='find'),
    path('register',views.register,name='register'),
]