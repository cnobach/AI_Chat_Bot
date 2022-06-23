from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('chatbot/index.html')
    context = {
        'heading': 'AI Chat Bot'
    }
    return render(request, 'chatbot/index.html', context)