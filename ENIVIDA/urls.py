
from django.contrib import admin
from django.urls import path

from .views import index, login, signup, filetender, activetender, Uindex, about, cancelledtender, recruitment, circular, events, contactus, media, adminlogin, adminsignup, AdminShowUser, AdminReq, AdminAddReq, Compare_Bids

urlpatterns = [
    path('', index, name='home'),
    path('login',login, name='login'),
    path('signup',signup),
    path('filetender',filetender, name = 'filetender'),
    path('activetender',activetender),
    path('U.index', Uindex, name='Uhome'),
    path('about', about, name = 'about'),
    path('cancelledtender', cancelledtender),
    path('recruitment', recruitment, name= 'rec'),
    path('circular', circular, name='circular'),
    path('events', events, name='events'),
    path('contactus', contactus, name='contactus'),
    path('media', media, name='media'),
    path('adminsignup', adminsignup ),
    path('adminlogin', adminlogin),
    path('AdminShowUser', AdminShowUser, name = 'AdminShowUser'),
    path('AdminReq', AdminReq, name='AdminReq'),
    path('AdminAddReq', AdminAddReq, name='AdminAddReq'),
    path('Compare_Bids', Compare_Bids, name='Compare_Bids')

]
