from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from .models import *
# Create your views here.

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    template_name= 'accounts/profile.html'
    habitude = HabitudeAlimentaire.objects.filter(user=request.user)
    
    context = {
        'session' : habitude,
    }
    
    return render(request, template_name,context)