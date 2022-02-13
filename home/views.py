from django.shortcuts import render
from django.contrib import messages


def index(request):
    """ View to return index.html """

    messages.success(request, 'Welcome Home!')

    return render(request, 'home/index.html')
