from django.shortcuts import render, redirect
from django.http import HttpResponse
from hmng.models import Patient
import json
from datetime import date
from django.core.exceptions import ValidationError


def welcome(request):
    return render(request, "welcome.html")

def PatientRegistrationForm(request):
    return render(request, 'PatientRegistrationForm.html')

def PatientRegistration(request):
    from django.core.exceptions import ValidationError

def PatientRegistration(request):
    user_status = None
    if request.method == 'POST':
        try:
            pid=request.POST.get('Pid')
            first_name_p = request.POST.get('first_name_p')
            last_name_p = request.POST.get('last_name_p')
            dob_p = request.POST.get('dob_p')
            gender_p = request.POST.get('gender_p')
            mob_num_p = request.POST.get('mob_num_p')
            address = request.POST.get('address')
            age_p = request.POST.get('age_p')

            if Patient.objects.filter(first_name_p=first_name_p, last_name_p=last_name_p).exists():
                user_status = 1  # User already exists
            else:
                patient = Patient(
                    first_name_p=first_name_p,
                    last_name_p=last_name_p,
                    dob_p=dob_p,
                    gender_p=gender_p,
                    mob_num_p=mob_num_p,
                    address=address,
                    age_p=age_p,
                )
                patient.save()
                user_status = 2  # User created successfully
        except ValidationError as e:
            print("Validation error:", e)
            user_status = 3  # Validation error
        except Exception as e:
            print("Error:", e)
            user_status = 3  # Other errors
    else:
        user_status = 3  # Not a POST request

    return render(request, 'home.html', {'userStatus': user_status,'first_name_p':first_name_p,'last_name_p':last_name_p,'pid':pid})

def loginView(request):
    if request.method == 'POST':
        first_name_p = request.POST.get('first_name_p')
        last_name_p = request.POST.get('last_name_p')
        dob_p = request.POST.get('dob_p')  # dob_p as a string from POST

        # Convert dob_p to a date object (if necessary)
        try:
            dob_p = date.fromisoformat(dob_p)  # Parse 'YYYY-MM-DD' format
        except ValueError:
            login_error = "Invalid Date Format. Please use YYYY-MM-DD."
            return render(request, 'loginView.html', {'loginError': login_error})

        # Query the patient
        patient = Patient.objects.filter(
            first_name_p=first_name_p,
            last_name_p=last_name_p,
            dob_p=dob_p
        ).first()

        if patient is None:
            login_error = "Invalid Username or Password"
            return render(request, 'loginView.html', {'loginError': login_error})
        else:
            # Successful login
            request.session['username'] = patient.first_name_p
            request.session['name'] = patient.last_name_p
            # Store dob_p as a string in ISO format
            request.session['dob_p'] = patient.dob_p.isoformat()
            return redirect('hmng:home')

    return render(request, 'loginView.html')
   
def DoctorRegistrationForm(request):
    return render(request, 'DoctorRegistrationForm.html')

def DoctorRegistration(request):
    # Handle doctor registration logic
    pass

def Nurse(request):
    # Handle nurse-related logic
    return render(request, 'home.html')


def apint(request):
    return render(request, 'appotement.html')
