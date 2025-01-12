from django.urls import path
from hmng.views import *
import json
from datetime import date

app_name = 'hmng'

urlpatterns = [
    path('', welcome, name='welcome'),
    path('new-patient', PatientRegistrationForm, name='registrationForm'),
    path('store-patient', PatientRegistration, name='storePatient'),
    path('login', loginView, name='loginView'),
    path('new-doctor', DoctorRegistrationForm, name='registrationFormDoctor'),
    path('store-doctor', DoctorRegistration, name='storeDoctor'),
    path('home', Nurse, name='home'),
    path('apint',apint,name='apint'),
    path('logout/',logoutView, name='logout'),
    
]
