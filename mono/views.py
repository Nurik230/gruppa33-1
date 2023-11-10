from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime

from .forms import CreateMobileForm, ReviewCreateForm
from .models import Mobile, Review


def mobile_list_view(request):
    if request.method == 'GET':
        mobile_value = Mobile.objects.all()
        html_file_name = 'mobile/mobile.html'
        context = {
            'mobile_key': mobile_value
        }
        return render(request, template_name=html_file_name, context=context)


def mobile_detail_view(request, id):
    mobile = get_object_or_404(Mobile, id=id)
    if request.method == 'GET':
        context_data = {"mobile": mobile,
                        "form": ReviewCreateForm}
        return render(request, template_name='mobile/mobile_detail.html', context=context_data)


    elif request.method == "POST":
        data = request.POST
        form = ReviewCreateForm(data)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            Review.objects.create(
                text=cleaned_data.get('text'),
                mobile_id=id
            )
            context_data = {"mobile": mobile,
                            "form": ReviewCreateForm}

    return render(request, template_name='mobile/mobile_detail.html', context=context_data)


def mobile_create_views(request):
    if request.method == 'GET':
        context_data = {
            'form': CreateMobileForm
        }

        return render(request, 'mobile/create.html', context=context_data)
    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = CreateMobileForm(data, files)

        if form.is_valid():
            cleaned_data = form.cleaned_data
            Mobile.objects.create(
                image=cleaned_data.get('image'),
                title=cleaned_data.get('title'),
                description=cleaned_data.get('description'),
                cost=cleaned_data.get('cost'),
                director=cleaned_data.get('director'),
                number_of_page=cleaned_data.get('number_of_page'),
            )
            return redirect('/mobile/')
        return render(request, 'mobile/create.html', context={'form': form})
