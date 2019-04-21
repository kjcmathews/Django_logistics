from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
path('', views.logistic_reg, name="logistic"),
path('update/<int:pk>', views.logistic_update, name="logistic_update"),
path('delete/<int:pk>', views.logistic_delete, name="logistic_delete")

]