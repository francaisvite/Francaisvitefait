from django.shortcuts import render, render_to_response
from django.shortcuts import HttpResponse, HttpResponseRedirect
from .forms import SubmitDocForm, LoginForm
from .models import Login, SubmitDoc
from django.template import context, RequestContext
from _datetime import date
from datetime import datetime
import os
import re
import docx
from docx import Document
from django.http.response import HttpResponseRedirect
import logging
from .traite import get_docx_text
from paypal.standard.forms import PayPalPaymentsForm
from django.core.urlresolvers import reverse
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.utils import timezone
from django.db.transaction import commit



logger = logging.getLogger(__name__)
totals =0
    
def home(request):
    return render( request, "francais/home.html" , {})

def aboutUs(request):
    return render(request, "francais/AboutUs.html", {})
  
  
def newSubmit(request):
    save= False
    form = SubmitDocForm(request.POST, request.FILES)
    com =0
    compteur=0
    message ="bon"
    solution = ""
    counted=0
    stud = False
    amount_stu = 0.02
    amount_pro = 0.03
    
   
    if form.is_valid():
        submitDoc = SubmitDoc()
        submitDoc.firstName = form.cleaned_data['firstName'] 
        submitDoc.lastName = form.cleaned_data['lastName']
        submitDoc.email = form.cleaned_data['email']
        submitDoc.Stud_status = form.cleaned_data['Stud_status']
        submitDoc.uploadDoc = form.cleaned_data['uploadDoc'] 
#         submitDoc.like = form.cleaned_data["like"]  
        submitDoc.comment = form.cleaned_data['comment']
        submitDoc.save()
        save = True
#         data = request.FILES["uploadDoc"]
        pathy = submitDoc.uploadDoc.path
        solution= get_docx_text(pathy)
        counted = len(solution.split())
        type_of_doc =  form.cleaned_data['Stud_status']
        
        if  form.cleaned_data['Stud_status'] == "on":
            stud = True
            totals = round(counted*0.02, 2)
        else:
            stud = False
            totals = round(counted *0.03, 2)
        
    else:
        form = SubmitDocForm()
         
    return render(request, 'francais/saved.html', locals())
 
# def paySuccess(request, pk):
#     if request.POST.get("custom", "") =="posted":
#         
#         
#     return render(request, 'francais/paysuccess.html', locals())



def login(request):
    username= "not logged on"
      
    MyLoginForm = LoginForm(request.POST)
         
    if MyLoginForm.is_valid():
        lologin =Login()
        lologin.username = MyLoginForm.cleaned_data['username']
        
    else:
        MyLoginForm = LoginForm()
            
    response= render(request, "francais/loggedin.html", {"username": username})
    
    response.set_cookie('last_connection', datetime.now())
    response.set_cookie('username', datetime.now())
            
    return response


def formView(request):
    
    if "username" in request.COOKIES and "last_connection" in request.COOKIES:
        username = request.COOKIES['username']
        last_connection = request.COOKIES["last_connection"]
        
        last_connection_time = datetime.strptime(last_connection[:-7], "%Y-%m-%d %H:%M:%S")
        
        if (datetime.now() - last_connection_time).seconds <10 :
            return render (request, "francais/loggedin.html", {"username" : username})
        else:
            return render (request, "francais/login.html", {})
        
    else: 
        return render(request, "francais/login.html")
    





# print(content) 


    
    
    