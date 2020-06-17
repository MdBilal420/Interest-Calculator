from django.shortcuts import render
from django.http import HttpResponse
from interest.models import Info


def index(request):
    if request.method == 'POST':
        principle = request.POST.get('principle')
        addition = request.POST.get('addition')
        rate = request.POST.get('rate')
        time = request.POST.get('time')
        rr = 1
        float(rr)
        rr  = rate*0.01
        i = 1
        while i < time:
            principle = ( principle + addition)*(1+rr)
            i += 1
    return render(request, 'interest/index.html')


