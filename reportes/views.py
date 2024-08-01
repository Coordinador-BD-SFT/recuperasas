from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms
import os
# Create your views here.


def index(request):
    tipos_reporte = models.TipoReporte.objects.all()

    return render(
        request,
        'index.html',
        context={'tipos_reporte': tipos_reporte}
    )


def reporte(request, tipo_reporte_name):
    reportes = models.Reporte.objects.filter(report_type=tipo_reporte_name)
    report_type = models.TipoReporte.objects.get(name=tipo_reporte_name)

    return render(
        request,
        'reportes.html',
        context={
            'reportes': reportes,
            'report_type': report_type,
        }
    )


def reporte_form(request, tipo_reporte_name):
    report_type = get_object_or_404(models.TipoReporte, name=tipo_reporte_name)
    if request.method == 'POST':
        form = forms.Reporteform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/reportes/{tipo_reporte_name}')
    else:
        form = forms.Reporteform()

    return render(
        request,
        'reporte_form.html',
        context={
            'form': form,
            'report_type': report_type,
        }
    )


def reporte_detalle(request, tipo_reporte_name, reporte_id):
    report_type = get_object_or_404(models.TipoReporte, name=tipo_reporte_name)
    reporte = get_object_or_404(models.Reporte, id=reporte_id)
    file_names = {
        'chats_file_name': os.path.basename(reporte.chats_file.name) if reporte.chats_file else 'No file',
        'envio_sms_file_name': os.path.basename(reporte.envio_sms_file.name) if reporte.chats_file else 'No file',
    }

    return render(
        request,
        'reporte_detalle.html',
        context={
            'reporte': reporte,
            'report_type': report_type,
            'file_names': file_names
        }
    )
