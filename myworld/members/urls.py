from django.urls import path
from . import views

urlpatterns = [
   
       path('aa', views.aa, name='aa'),
       path('bb', views.bb, name='bb'),
       path('cc', views.cc, name='cc'),
       path('add', views.add, name='add'),
       path('all', views.all, name='all'),
       path('addrecord/', views.addrecord, name='addrecord'),
    
       path('', views.index, name='index'),
]