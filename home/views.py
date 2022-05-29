from django.shortcuts import render
from django.contrib import messages


def index(request):
    """ View to return index.html """

    # controls the transparency of the header area
    style_switch = True

    all_content = {
        'style_switch': style_switch,
    }



    return render(request, 'home/index.html', all_content)
