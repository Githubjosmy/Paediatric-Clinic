from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='homes'),
    path('about/',views.about,name='about'),
    path('contact/', views.contact, name='contact'),




    path('admin_home/', views.admin_home, name='admin_home'),
    path('add_doctor/',views.add_doctor,name='add_doctor'),
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('edit_doctor/<int:pid>',views.edit_doctor,name='edit_doctor'),
    path('delete_doctor/<int:pid>',views.delete_Doctor, name='delete_doctor'),
    path('add_patient', views.add_patient, name='add_patient'),
    path('view_patient', views.view_patient, name='view_patient'),
    path('edit_patient/<int:pid>', views.edit_patient, name='edit_patient'),
    path('delete_patient/<int:pid>',views. delete_Patient, name='delete_patient'),
    path('view_appointment', views.view_appointment, name='view_appointment'),

]