from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from Paediatric_app.models import *
from .models import *


def Register(request):
    if request.method == 'POST':
        f_name = request.POST['First_name']
        l_name = request.POST['Last_name']
        username = request.POST['Username']
        e_mail = request.POST['Email']
        password = request.POST['Password']
        confirm_password = request.POST['Confirm Password']
        # Validation
        error_msg = None
        if not f_name:
            error_msg = "First name required"
        elif len(f_name) < 4:
            error_msg = "First name must be 4 characters long or more"
        elif not l_name:
            error_msg = "Last name required"
        elif len(l_name) < 1:
            error_msg = "Last name must be 4 characters long or more"

        elif len(username) < 8:
            error_msg = "Username must be 8 characters long"

        elif len(e_mail) < 8:
            error_msg = "Email must be 8 characters long"

        elif len(password) < 8:
            error_msg = "Password must be 8 characters long"

        elif User.objects.filter(email=e_mail).exists():
            error_msg = "Email already taken"

        elif User.objects.filter(username=username).exists():
            error_msg = "Username already exists"

        elif password != confirm_password:
            error_msg = "Password not matching"

        values = {

            'vf_name': f_name,
            'vl_name': l_name,
            'v_username': username,
            'v_password': password,
            'v_email': e_mail,
            'vc_password': confirm_password
        }
        if not error_msg:
            u = User.objects.create_user(first_name=f_name, last_name=l_name, email=e_mail, username=username,
                                         password=password)
            u.save()
            return redirect("Logins")
        else:
            data = {
                'values': values,
                'error_msgs': error_msg,
            }

            return render(request, 'Register.html', data)

    else:
        return render(request, 'Register.html')


def Login(request):
    if request.method == 'POST':
        l_username = request.POST['Username']
        l_password = request.POST['Password']

        if l_username == 'josmy' and l_password == 'josmy':
            return redirect('admin_home')
        else:
            user_login = auth.authenticate(username=l_username, password=l_password)
            if user_login is not None:
                auth.login(request, user_login)
                return render(request, 'index.html')

            else:
                error_msg = "Invalid details"
                return render(request, 'login.html', {'error': error_msg})
    else:
        return render(request, 'login.html')


def appointment(request):
    doctor = Doctors.objects.values_list('name', flat=True).distinct()
    specialize = Doctors.objects.values_list('specialize', flat=True).distinct()
    # print(doctor)
    return render(request, "appointment.html", {'doctor': doctor, 'specialize': specialize})


def patient_detail(request):
    if request.method == "POST":
        d_name = request.POST['doctor']
        s_name = request.POST['special']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        e_mail = request.POST['email']
        p_hone = request.POST['phone']
        dob_name = request.POST['dob']
        blood_type_name = request.POST['blood_type']
        add_name = request.POST['address']
        g_name = request.POST['gender']
        pre_polio_name = request.POST['polio']
        ap_date_name = request.POST['apt_date']
        ap_time_name = request.POST['apt_time']
        patient_data = Patient_data(doctor_name=d_name, spec=s_name, first_name=f_name, Last_name=l_name, Email=e_mail,
                                    Phone_no=p_hone, DOB=dob_name, Address=add_name, BLOOD_TYPE=blood_type_name,
                                    Gender=g_name,
                                    Prev_dose=pre_polio_name, Appt_date=ap_date_name, Appt_time=ap_time_name)
        patient_data.save()
        data = Patient_data.objects.get(first_name=f_name, Phone_no=p_hone)
        print(data.id)

        return render(request, 'patient_detail.html', {'data': data})

#
# def patient_profile(request, uid):
#     profile = User.objects.get(id=uid)
#     return render(request, 'patient_profile.html', {'profile': profile})


def Logout(request):
    auth.logout(request)
    return redirect('/')
