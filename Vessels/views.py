from django.shortcuts import render
from django.http import HttpResponse
from .models import Vessel, VesselSchedule, PortCall
from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'Vessels/base.html')


def Vessels(request):
    vessels = Vessel.objects.all()
    context = {'vessels': vessels}
    return render(request, 'Vessels/Vessels.html', context)


#def index(request):
    #return HttpResponse('Hello from Vessels');


def Vessel_info(request, vessel_name):
    return HttpResponse('Showing info for vessel ' + vessel_name);


def port_info(request):
    ports = PortCall.objects.all()
    port_list = ', '.join([p.port for p in ports])
    return HttpResponse('Here is a list of our ports: ' + port_list);


# MIGHT BE AWFUL
def charleston_vessels(request):
    port_calls = PortCall.objects.filter(port='Charleston')
    vessels = set([port_call.vessel_schedule.vessel for port_call in port_calls])
    return render(request, 'Vessels/Charleston.html', {'vessels': vessels})


def vessel_schedule(request, vessel_id):
    vessel = Vessel.objects.get(id=vessel_id)
    schedules = VesselSchedule.objects.filter(vessel=vessel)
    context = {
        'vessel': vessel,
        'schedules': schedules,
    }
    return render(request, 'Vessels/vessel_schedule.html', context)
