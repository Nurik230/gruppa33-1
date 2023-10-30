from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Mobile


def mobile_list_view(request):
    if request.method == 'GET':
        mobile_value = Mobile.objects.all()
        html_file_name = 'mobile/mobile.html'
        context = {
            'mobile_key': mobile_value
        }
        return render(request, template_name=html_file_name, context=context)


def mobile_detail_view(request, id):
    if request.method == 'GET':
        context_data = {"mobile": get_object_or_404(Mobile, id=id)}
        return render(request, template_name='mobile/mobile_detail.html', context=context_data)

