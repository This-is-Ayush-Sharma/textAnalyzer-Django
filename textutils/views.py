# from django.http import HttpResponse
from django.shortcuts import render
import string



def index(request):
    params = {"output": 'Output appears here'}
    return render(request, 'index.html', params)


def removePunc(request):
    # return HttpResponse("Removepunc")
    # get the text
    djtext = request.GET.get('text', 'default')
    # analyze the text
    params = {"output": ''.join(i for i in [char for char in djtext if char not in string.punctuation])}
    

    return render(request, 'index.html', params)

def capitalizefirst(request):
    djtext = request.GET.get('text', 'default')
    params = {"output": djtext.capitalize()}
    return render(request, 'index.html', params)

def newlineremover(request):
    djtext = request.GET.get('text', 'default')
    params = {"output": djtext.replace('\n','').replace("\r","")}
    return render(request, 'index.html', params)

def spaceremover(request):
    djtext = request.GET.get('text', 'default')
    params = {"output": djtext.replace(" ","")}
    return render(request, 'index.html', params)

def charcount(request):
    djtext = request.GET.get('text', 'default')
    params = {"output": f'Number of characters are {len(djtext)}'}
    return render(request, 'index.html', params)