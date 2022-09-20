from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from members.models import Members
from django.urls import reverse 

def index(request):
    return HttpResponse("Hello world!")

def aa(request):
    return HttpResponse("Hello world! From AA")    


def bb(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def cc(request):
    template = loader.get_template('one.html')
    return HttpResponse(template.render())    


def add(request):
     mymembers = Members.objects.all().values()
     context = { 'mymembers': mymembers,  }
     template = loader.get_template('add.html')
     return HttpResponse(template.render(context, request))

def all(request):
    mymembers = Members.objects.all().values()
    output = ''
    for x in mymembers:
      output +=' <br/> '+ x["firstname"]
    return HttpResponse(output)    

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('all'))