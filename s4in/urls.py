from django.urls import path

from s4in import views

urlpatterns = [
    path('',views.index,name="home"),
    path('detail/<str:pk>/',views.detail,name="detail"),
    path('projects/',views.projects,name="projects"),

]