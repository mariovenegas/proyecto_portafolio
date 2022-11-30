from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views.generic import View

from django.http import FileResponse
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from clients.models import Client
from professionals.models import Professional
from contracts.models import Contract

from advisorys.models import Advisory
from capacitations.models import Capacitation
from visits.models import Visit
from django.http import HttpResponse
import json

# Create your views here.
def reports(request):

    clients = Client.objects.all().order_by('id')

    if request.method == 'POST':
        client = request.POST.get('client')

        selected_client = Client.objects.get(name=client)
        try:
            advisorys = Advisory.objects.filter(client=selected_client.id).order_by('id')
        except:
            advisorys = None

        try:
            capacitations = Capacitation.objects.filter(client=selected_client.id).order_by('id')
        except:
            capacitations = None

        try:
            visits = Visit.objects.filter(client=selected_client.id).order_by('id')
        except:
            visits = None
            


        if 'pdf' in request.POST:

            buf = io.BytesIO()
            c = canvas.Canvas(buf, pagesize=letter,bottomup=0)
            textob = c.beginText()
            textob.setTextOrigin(inch,inch)
            textob.setFont("Helvetica",18)
            textob.textLine("Reporte cliente " + selected_client.name)
            textob.textLine("====================================")
            textob.textLine(" ")

            textob.setFont("Helvetica",14)
            textob.textLine("Listado de Visitas")
            textob.textLine("-----------------------------")
            textob.setFont("Helvetica",12)
            lines = []
            for visit in visits:
                lines.append("Fecha : " + str(visit.date) + "     Profesional : " + str(visit.professional.name))
                lines.append("Razon : " + str(visit.reason))
                lines.append("Estado: " + str(visit.state))
                lines.append(" ")

            for line in lines:
                textob.textLine(line)
            c.drawText(textob)

            textob.setFont("Helvetica",14)
            textob.textLine("Listado de Asesorias")
            textob.textLine("-----------------------------")
            textob.setFont("Helvetica",12)
            lines = []
            for advisory in advisorys:
                lines.append("Fecha : " + str(advisory.date) + "     Profesional : " + str(advisory.professional.name))
                lines.append("Tema  : " + str(advisory.topic))
                lines.append("Estado: " + str(advisory.state))
                lines.append(" ")

            for line in lines:
                textob.textLine(line)
            c.drawText(textob)

            textob.setFont("Helvetica",14)
            textob.textLine("Listado de Capacitaciones")
            textob.textLine("-----------------------------")
            textob.setFont("Helvetica",12)
            lines = []
            for capacitation in capacitations:
                lines.append("Fecha : " + str(capacitation.date) + "     Profesional : " + str(capacitation.professional.name))
                lines.append("Tema  : " + str(capacitation.topic))
                lines.append("Estado: " + str(capacitation.state))
                lines.append(" ")

            for line in lines:
                textob.textLine(line)
            c.drawText(textob)

            c.showPage()
            c.save()
            buf.seek(0)
            return FileResponse(buf, as_attachment=True, filename='reporte.pdf')
    else:
        advisorys = None
        capacitations = None
        visits = None
        client = None

    
    return render(request, "reports/reports.html", {'clients':clients,'selected_client':client,'advisorys':advisorys,'capacitations':capacitations,'visits':visits})
