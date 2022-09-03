import sys
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from base64 import b64encode, b64decode
from cpp import *
from python import *


# Create your views here.

class CodeUpload(APIView):
    def validate(self):
        data = json.loads(self.request.body.decode('utf-8'))
        self.language = data.get("language", '')
        self.code_content = data.get("code", '')
        self.custom_input = data.get("custom_input", '')

        #print(self.language, self.code_content)

    def return_genric_response(self):
        return Response(self.result, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        self.validate()
        self.result = {'data':self.start_compiling()}
        #self.result = {'output': self.output_std}
        return self.return_genric_response()

    def start_compiling(self):
        if self.language == "cpp":
            return compile_code_cpp(self.code_content, self.custom_input)
        elif self.language == "python":
            return compile_code_python(self.code_content, self.custom_input)

