#  I HVE CREATED THIS FILE - MANISH
from django.http import HttpResponse
from django.shortcuts import render

def ex1(request):
    return HttpResponse('''
    <a href="https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&difficulty%5B%5D=0&difficulty%5B%5D=1&page=1">Practice on GeeksforGeeks</a><br>
    <a href="https://www.hackerrank.com/dashboard">Practice on HackerRank</a><br>
    <a href="https://www.google.com/">Open GOOGLE</a><br>
    <a href="https://gaana.com/">Listen Music With Gaana</a><br>
    <a href="https://www.linkedin.com/feed/">Make Profile on Linkedin</a><br>
    <a href="http://127.0.0.1:8000/">Remove punctuation mark from text</a>
    ''')

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!"#$%&'()*+,-._/:;<=>?@[]^`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+ char
        parms = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        parms = {'purpose': 'Change all letter to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!= "\r":
                analyzed = analyzed + char
        parms = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        parms = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = 0
        for char in djtext:
            if char.isalnum():
                analyzed = analyzed + 1
        parms = {'purpose': 'count character', 'analyzed_text': analyzed}

    if charcount != "on" and extraspaceremover!= "on" and newlineremover!= "on" and fullcaps!= "on" and removepunc!= "on":
        return HttpResponse("Please check the Remove punctuation <br> <a href='http://127.0.0.1:8000/'>Back to home</a>")
    return render(request, 'analyze.html', parms)


