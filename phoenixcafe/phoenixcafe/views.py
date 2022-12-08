#!/usr/bin/python3
import datetime

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse

# This view will return "Welcome to the Phoenix Cafe!" as text
def welcome(request):
    return HttpResponse("Welcome to the Phoenix Cafe!")

# This view will return "Z-z-z-z-z-z-z!" when called.
def sleepy(request):
    return HttpResponse("Z-z-z-z-z-z-z!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)  # we are not returning a static string

