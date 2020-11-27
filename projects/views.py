from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
# @login_required(login_url='/accounts/register/')
def index(request):
    date = dt.date.today()
    heading = "Welcome to Shitandi Awward Application"
    
    return render(request, 'home.html', {"date": date, "heading":heading})
