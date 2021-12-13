from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.toplanti_form,name='toplanti_insert'),
    path('<int:id>/', views.toplanti_form,name='toplanti_update'),
    path('delete/<int:id>',views.toplanti_delete,name='toplanti_delete'),
    path('list/',views.toplanti_list,name='toplanti_list')
]
