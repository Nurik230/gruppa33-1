from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from . import models

def mobileListView(request):
    mobile_value = models.Mobile.objects.all()
    html_file_name = 'mobile/mobile.html'
    context = {
        'mobile_key': mobile_value
    }
    return render(request, html_file_name, context)




def helloView(reguest):
    return HttpResponse('<h1>Hello!It is my project</h1>')
def now_dateView(reguest):
    data11 = datetime.now().date()
    return HttpResponse(data11)
def goodbyView(reguest):
    return HttpResponse('<h1> Goodby user! </h1>')


