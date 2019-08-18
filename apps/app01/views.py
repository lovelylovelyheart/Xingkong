from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from .tasks import add


class MyHouse(View):
    def get(self, request):
        return HttpResponse('OK')


def book(request):
    add.delay(4, 7)
    return HttpResponse('OK')
