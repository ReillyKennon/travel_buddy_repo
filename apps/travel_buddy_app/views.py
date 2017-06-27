# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import User, Trip
import bcrypt
from django.db.models import Q
# Create your views here.

def index(request):
    try:
        error_messages = request.session['context']
    except:
        error_messages = {}
    return render(request, 'travel_buddy_app/index.html', error_messages)

def register(request):
    context = {}
    new_user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=bcrypt.hashpw(request.POST['password'].encode('utf8'), bcrypt.gensalt()))
    try:
        new_user.full_clean()
    except ValidationError as error:
        for key in error:
            context[key[0]] = key[1][0]
    if request.POST['password'] != request.POST['password_confirm']:
        context['pw_mismatch'] = 'Passwords do not match'
    if context == {}:
        print ('********* No Registration Errors')
        new_user.save()
        context['result'] = 'Registration Complete!'
        request.session['context'] = context
        return redirect('/dashboard')
    else:
        context['result'] = 'Reigstration failed. Please try again.'
        request.session['context'] = context
        return redirect('/')

def dashboard(request):

    database = {
        "trips": Trip.objects.all()
    }
    return render(request, 'travel_buddy_app/dashboard.html', database)

def destination(request):
    # This needs to grab a specific trip connected by destination on dashboard template
    destination_info = {

    }
    return render(request, 'travel_buddy_app/destination.html', destination_info)

def addplan(request):
    return render(request, 'travel_buddy_app/addplan.html')

def login(request):
    request.session['first_name'] = request.POST['first_name']
    authenticate = User.objects.get(email=request.POST['email'])
    print authenticate.password.encode('utf8')
    user_pwhash = bcrypt.hashpw(request.POST['password'].encode('utf8'), authenticate.password.encode('utf8'))
    print user_pwhash
    if authenticate.password == user_pwhash:

        print ("*************************")
        print (User.objects.get(email=request.POST['email']))
        return redirect('/dashboard')
    else:
        request.session['context'] = {'failed_login': 'Incorrect email or password'}
        return redirect('/')

def logout(request):
    request.session.clear
    return redirect('/')

def home(request):
    return redirect('/dashboard')

def add(request):
    Trip.objects.add(request.POST)
    return redirect('/dashboard')

# def join(request):
#
