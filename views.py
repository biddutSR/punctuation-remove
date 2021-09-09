from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse('about')
def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc =request.GET.get('removepunc','off')
    # analyzed = djtext
    punctuation =""" !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ """
    analyzed = ""
    for char in djtext:
        if char not in punctuation:
            analyzed=analyzed+char
    params = {'purpose': 'removed punctuations', 'analyzed_text': analyzed}
    return render(request,'analyze.html',params)
