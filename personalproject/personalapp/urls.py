from .import views
from django.urls import path
urlpatterns = [
path('', views.demo, name='demo')
# path('home/', views.home)
# path('operator/', views.addition, name='addition'),
# path('', views.subtraction, name='subtraction'),
# path('', views.multiplication, name='multiplication'),
# path('', views.division, name='division')
]

