from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import doctor, room, patient

from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/')

# Create your views here.
def index(request):
	return render(request, 'hospitalmanagementsystem/index.html')

def userinfo(request):
  return render(request, 'hospitalmanagementsystem/userinfo.html')

def doctorlist(request):
  
  docs = doctor.objects.all()
  
  template = loader.get_template('hospitalmanagementsystem/doctors.html')
  context = {'docs': docs}
  
  return HttpResponse(template.render(context, request))

def roomlist(request):
  
  roomslist = room.objects.all()
  
  template = loader.get_template('hospitalmanagementsystem/rooms.html')
  context = {'roomslist': roomslist}
  
  return HttpResponse(template.render(context, request))

def patientlist(request):
    patientslist = patient.objects.all()
  
    template = loader.get_template('hospitalmanagementsystem/patients.html')
    context = {'patientslist': patientslist}
  
    return HttpResponse(template.render(context, request))