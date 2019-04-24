from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt


from .models import InputRowModel, ExportRowModel

# problem 2 - input a, b through rest api and respond with a*b
def mul_ab(request, **kwargs):
    a = kwargs['a']
    b = kwargs['b']
    data = {"mul": a*b}
    return JsonResponse(data)

class UploadFileForm(forms.Form):
    file = forms.FileField

@csrf_exempt
class UploadExcel(View):

    def __init__(self, **kwargs):
        print("----------------------------->here<---------------------------------")
        return super().__init__(**kwargs)
    
    def post(self, request):
        if (request.method != 'POST'):
            return render(request, 'uploadFile.html', {'foo':'bar'})
        else:
            return render(request, 'uploadFile.html', {'foo':'bar'})