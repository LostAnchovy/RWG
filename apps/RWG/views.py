from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
  if not 'random_gen'in request.session:
    request.session['random_gen']= get_random_string(length=14)
  if not 'counter' in request.session:
    request.session['counter'] =1
  context ={
    "random_gen":request.session['random_gen'],
    "counter" : request.session['counter'],
    }
  return render(request,'rwg.html',context)
    
def generate(request):
  request.session['counter'] +=1
  request.session['random_gen']= get_random_string(length=14)
  return redirect('/')

def reset(request):
  del request.session['counter']
  del request.session['random_gen']
  return redirect('/')
