from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from base64 import b64encode, b64decode





# Create your views here.

class CodeUpload(APIView):
    def validate(self):
        data = json.loads(self.request.body.decode('utf-8'))
        self.language = data.get("language", '')
        self.code_content = data.get("code",'')
        print(self.language, self.code_content)

    def return_genric_response(self):
        return Response(self.result, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        self.validate()
        self.result = {'msg': 'registration success'}
        return self.return_genric_response()


#"language":"sfsdf",
#"code":"dfdf"}