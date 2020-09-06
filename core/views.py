from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(
        request,
        template_name = 'hello.html',
        context = {'adjectives': [14, 56 , 43, 94, 12, 3, 113]}
    )

