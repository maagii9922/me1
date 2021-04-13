from django.http import HttpResponse
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import re
import random
import requests

 
def home(request):
    return HttpResponse('oooooook')
VERIFY_TOKEN='123456'
class Botview(generic.View):
    def get(self,request,*args,**kwargs):
        if self.request.GET['hub.verify_token']==VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')
