
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path("<int:pk>/", views.home1, name="home1"),
    path('home2',views.home2,name='home2'),
    path('home3',views.home3,name='home3'),
    path('home4',views.home4,name='home4'),
    path('home5',views.home5,name='home5'),
    path('home6',views.home6,name='home6'),
    path('home7',views.home7,name='home7'),
    path('home8',views.home8,name='home8'),
    path('home9',views.home9,name='home9'),
    path('home10',views.home10,name='home10'),
    path('home11',views.home11,name='home11'),
    path('home12',views.home12,name='home12'),
    path('home13',views.home13,name='home13'),
    path('home14',views.home14,name='home14'),
    path('home15',views.home15,name='home15'),
]
