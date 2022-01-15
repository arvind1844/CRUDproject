from django.urls import path
from . import views

urlpatterns = [
    path('',views.addshowform, name="home"),
    path('delete/<int:id>',views.deletedata, name="delete"),
    path('update/<int:id>',views.updatedata, name="update"),
    
]
