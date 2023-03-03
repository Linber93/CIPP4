from django.shortcuts import render

# Create your views here.


def get_landing_page(request):
    return render(request, "linberp4/base.html")
