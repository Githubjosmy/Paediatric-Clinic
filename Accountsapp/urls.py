from django.urls import path
from . import views

urlpatterns = [

    path('Register/', views.Register, name='Registers'),
    path('Login/', views.Login, name='Logins'),
    path('Logout/', views.Logout, name='Logouts'),

    path('Appointment/',views.appointment,name='Appointments'),
    path('patient_detail/',views.patient_detail,name='patient_detail'),
    # path('patient_profile/<int:uid>',views.patient_profile,name='patient_profile'),


]