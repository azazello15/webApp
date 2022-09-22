from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Channel


def frontpage(request):
    channels = Channel.objects.all()
    return render(request, 'myApp/index.html')


def create(request):
    if request.method == 'POST':
        channels = Channel()
        channels.channel_name = request.POST.get('channel_name')
        channels.channel_img = request.POST.get('channel_img')
        channels.channel_url = request.POST.get('channel_url')
        channels.channel_stat = request.POST.get('channel_stat')
        channels.channel_err = request.POST.get('channel_err')
        channels.channel_crm = request.POST.get('channel_crm')
        channels.channel_coverage = request.POST.get('channel_coverage')
        channels.channel_description = request.POST.get('channel_description')
        channels.channel_category = request.POST.get('channel_category')
        channels.save()
    return HttpResponseRedirect('/')
