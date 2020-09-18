from django.shortcuts import render
from django.http import HttpResponse
from .models import patient


# Create your views here.
def index(request):
    patientsITD= patient.objects.all()
    print(patientsITD)
    params = {'patient':patientsITD}
    return render(request, 'patient/index.html', params)


def medician(request):
    name1 = request.GET.get('Pname', 'default')
    Mname = request.GET.get('Medi', 'Huma Medical')
    dic = {'Pname': name1, 'medi': Mname}
    if(name1 == 'Deo')or (name1 == 'Harsh Jain')or (name1 == 'Shubham gilda')or (name1 == 'Ashwath Jadhav'):
        return render(request, 'patient/medician.html',dic)
    else:
        patientsITD = patient.objects.all()
        params = {'patient': patientsITD}
        return render(request, 'patient/index.html', params)


def medical(request):
    MSname = request.GET.get('Medi', 'default')
    dic2 = {'madi': MSname}
    return render(request, 'patient/medical.html',dic2)



def help(request):
    return render(request, 'patient/help.html')



