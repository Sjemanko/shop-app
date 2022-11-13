from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def index(request):
    return HttpResponse("<h1>test1</h1>")


def second_test(request):
    return HttpResponse("<h1>test1</h1>")
