from django.shortcuts import render, redirect
from Accountsapp.models import Patient_data
from Paediatric_app.models import Doctors


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def admin_home(request):
    return render(request, 'admin_home.html')


def add_doctor(request):
    error = ""
    if request.method == 'POST':
        n = request.POST['name']
        sp = request.POST['special']
        m = request.POST['mobile']
        ad = request.POST['address']
        try:
            Doctors.objects.create(name=n, specialize=sp, mobile=m, address=ad)
            error = "no"
        except:
            error = "yes"

    return render(request, 'add_doctor.html', locals())


def view_doctor(request):
    doc = Doctors.objects.all()

    return render(request, 'view_doctor.html', locals())


def edit_doctor(request, pid):
    error = ""
    doctor = Doctors.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST['name']
        s1 = request.POST['special']
        m1 = request.POST['mobile']
        a1 = request.POST['address']

        doctor.name = n1
        doctor.specialize = s1
        doctor.mobile = m1
        doctor.address = a1

        try:
            doctor.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_doctor.html', {'error': error, 'doctor': doctor})


def delete_Doctor(request, pid):
    doctor = Doctors.objects.get(id=pid)
    doctor.delete()

    return redirect('view_doctor')


def add_patient(request):
    error = ""
    doctor = Doctors.objects.values_list('name', flat=True).distinct()
    print(doctor)
    specialize = Doctors.objects.values_list('specialize', flat=True).distinct()
    print(specialize)
    # unique_list = []
    # for i in specialize:
    #     if i not in unique_list:
    #         unique_list.append(i)
    # print(unique_list)
    if request.method == 'POST':
        d_n = request.POST['doctor_name']
        d_s = request.POST['doctor_specialize']
        fn = request.POST['f_name']
        ln = request.POST['l_name']
        e = request.POST['email']
        p = request.POST['phone']
        d = request.POST['dob']
        b = request.POST['blood_type']
        a = request.POST['address']
        g = request.POST['gender']
        pv = request.POST['polio']
        ap_date = request.POST['apt_date']
        ap_time = request.POST['apt_time']
        try:
            Patient_data.objects.create(doctor_name=d_n, spec=d_s, first_name=fn, Last_name=ln, Email=e, Phone_no=p,
                                        DOB=d,
                                        BLOOD_TYPE=b, Address=a, Gender=g, Prev_dose=pv, Appt_date=ap_date,
                                        Appt_time=ap_time)
            error = "no"
        except:
            error = "yes"
    return render(request, 'add_patient.html', locals())


def view_patient(request):
    pat = Patient_data.objects.all()
    d = {'pat': pat}
    return render(request, 'view_patient.html', d)


def edit_patient(request, pid):
    error = ""
    patient = Patient_data.objects.get(id=pid)
    if request.method == "POST":
        dn1 = request.POST['doctor_name']
        ds1 = request.POST['doctor_specialize']
        fn1 = request.POST['f_name']
        ln1 = request.POST['l_name']
        e1 = request.POST['email']
        ph1 = request.POST['phone']
        dob1 = request.POST['dob']
        gen1 = request.POST['gender']

        patient.doctor_name = dn1
        patient.spec = ds1
        patient.first_name = fn1
        patient.Last_name = ln1
        patient.Email = e1
        patient.Phone_no = ph1
        patient.DOB = dob1
        patient.Gender = gen1
        print(patient.Gender)
        print(patient.DOB)
        try:
            patient.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'edit_patient.html', locals())


def delete_Patient(request, pid):
    patient = Patient_data.objects.get(id=pid)
    patient.delete()

    return redirect('view_patient')


def view_appointment(request):
    appointment = Patient_data.objects.all()
    d = {'appointment': appointment}
    return render(request, 'view_appointment.html', d)
