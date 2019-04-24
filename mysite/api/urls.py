from django.urls import path
from .views import mul_ab, UploadExcel

urlpatterns = [
    path('mul/<int:a>/<int:b>/', mul_ab, name="mul_ab"),
    path('uploadExcel/', UploadExcel, name="UploadExcel")
]
