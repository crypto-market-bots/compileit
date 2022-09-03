from django.urls import path
from compiler.views import CodeUpload


urlpatterns = [
    path('codeRun/', CodeUpload.as_view(), name='codeUpload')
]
