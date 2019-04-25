from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
# to get the FileField for the html. 
from django import forms
# to use the excel
import django_excel as excel
#
import os
from django.conf import settings

# not used here...
# decorator written on a class, says which method it should be used on. 
from django.utils.decorators import method_decorator
# to deal with missing csrf token on POST requests 
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


# @method_decorator(csrf_exempt, name='dispatch')
class UploadExcel(View):

    export_sheet = None
      
    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['input-excel']
            return self.processExcel(request, form, filehandle)
    
    def get(self, request):
        form = UploadFileForm()
        return render(request, 'uploadFile.html', {
                'title': 'File Upload Form',
                'form': form,
                'export_sheet': self.export_sheet
            })

    def processExcel(self, request, form, filehandle):
        sheet = filehandle.get_sheet()
        export_data = []
        for row in sheet:
            export_row = []
            if row[0] == 'a':
                export_row.append(row[0])
                export_row.append(row[1])
                export_row.append('sum')
                export_row.append('product')
                export_data.append(export_row)
                continue
            
            export_row.append(int(row[0]))
            export_row.append(int(row[1]))
            export_row.append(row[0] + row[1])
            export_row.append(row[0] * row[1])
            export_data.append(export_row)
        export_sheet = excel.pe.Sheet(export_data)
        export_sheet.save_as('output-excel.xlsx')
        return render(request, 'uploadFile.html', {
            'title': 'File Upload Form',
            'form': form,
            'export_sheet': self.export_sheet
        })
          
    # return excel.make_response(, file_type='xlsx', file_name='output-excel.xlsx')

def downloadExcel(request):
    file_name = 'output-excel.xslx'
    print(settings.MEDIA_ROOT, 'asdfasdfasdf')
    with open(file_name, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + file_name
        return response