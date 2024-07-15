from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('ajax/load-projects/', views.load_projects, name='ajax_load_projects'),
    path('Propertyfilter/',views.filter_obj,name='filteroption'),
    path('Propertyfilter/ajax/load-projects/', views.load_projects, name='ajax_load_projects'),
    path('prop_view/<int:pid>', views.prop_view, name='prop_view'),
    path('contactus/<int:pid>', views.abt_us, name='prop_view')

    ]    
