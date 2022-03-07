from ast import Pass
import datetime
from email import message
from email.policy import EmailPolicy
from tkinter import N
from xmlrpc.client import DateTime
# from curses.ascii import EM
from django.shortcuts import redirect, render
from django.views import View
from .models import applied ,contact
from django.core.mail import send_mail
from bhartiya_airway.settings import EMAIL_HOST_USER
import sweetify

from django.contrib import messages


def home(request):
    # insert_data.save()

    return render(request , 'index.html' )
def applynow(request):

    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        City = request.POST.get('city')
        State = request.POST.get('state')
        Reference = request.POST.get('reference')
        resume = request.POST.get('CV')
        # resume1 = request.POST.get('CV')
        trm = request.POST.get('trm')
        Add = applied.objects.create(Name = Name , Email = Email , Mobile = Mobile , Address = address,City = City ,Reference = Reference , State = State,resume = resume , trm = trm )
        Add.save()
        Subject = 'Application'
        message2 = Name , 'We have received your application. We will notify you for further development regarding your application. Kindly keep in touch with us to get regular updates. We won’t let your skip any important information regarding your application.'
        send_mail(Subject,message2, EMAIL_HOST_USER, [Email], fail_silently = False)
        # message =  messages.info(request, 'Successfully Applied')
        sweetify.success(request, 'You did it', text='Good job! You successfully Applied', persistent='hey')
        return redirect('applynow')

        # print(resume)

    return render(request , 'applyNow.html' )
    

def about(request):
    # message =  messages.info(request, 'Successfully Applied')


    
    return render(request , 'about.html')

def contactdata(request):
    data = contact.objects.all()
    context = {
        'data' : data
    }
    return render(request , 'contactdata.html',context)

def career(request):

    return render(request , 'career.html')

def contactus(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Name = request.POST.get('Name')
        Message = request.POST.get('Message')
        Phone = request.POST.get('Phone')
        Subject = request.POST.get('Subject')
        message2 = 'We have .......'
        data = contact.objects.create(Name = Name , Email = Email , Message = Message , Phone = Phone , Subject = Subject)
        data.save()
        send_mail(Subject,message2, EMAIL_HOST_USER, [Email], fail_silently = False)
        sweetify.success(request, 'You did it', text='Good job! Message sent....', persistent='Hell yeah')


        return redirect('contact_us')
    return render(request , 'contactus.html' )
                 

def datatable(request):
    data = applied.objects.all()
    context = {
        'data':data
    }
    return render(request,'datatable.html' , context)
def datatableto(request):
    date = datetime.datetime.now().date()
    data = applied.objects.filter(Date = date )
    context = {
        'data':data
    }

    return render(request,'datatabletoday.html' , context)
def datatablewe(request):
    date = datetime.datetime.now().date()
    week = date.strftime("%V")
    data = applied.objects.filter(Date__week = week )
    # print(week)

    context = {
        'data':data
    }
    return render(request,'datatablewe.html' , context)

# import datetime
# date = datetime.datetime.today()
# week = date.strftime("%V")

# Entry.objects.filter(pub_date__week=week)    
def datatablemo(request):
    date = datetime.datetime.now().date()
    date_month = date.month
    data = applied.objects.filter(Date__month=date_month)
    context = {
        'data':data
    }
    return render(request,'datatablemonth.html' , context)

def dashboard(request):
    date = datetime.datetime.now().date()
    # print(date)
    data = applied.objects.filter(Date = date )
    data2 = applied.objects.all()
    data = data.count()
    data2 = data2.count()
    date_month = date.month
    datamonth = applied.objects.filter(Date__month=date_month)
    data_monthC = datamonth.count()
    context = {
        'data':data,
        'data2':data2,
        'datamonth':datamonth,
        'data_monthC':data_monthC,
    }
    return render(request,'dashboard.html', context)    
