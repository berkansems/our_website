from django.urls import path

from s4in import views

urlpatterns = [
    path('',views.index,name="home"),
    path('detail/<str:pk>/',views.detail,name="detail"),
    path('references/', views.references, name="references"),
    path('contacts/',views.contacts,name="contacts"),
    path('aboutus/',views.aboutUs,name="aboutus"),

]