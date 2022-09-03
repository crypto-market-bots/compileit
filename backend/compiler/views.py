import sys
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
        self.code_content = data.get("code", '')
        print(self.language, self.code_content)

    def return_genric_response(self):
        return Response(self.result, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        self.validate()
        self.solve()

        self.result = {'output': self.output_std}
        return self.return_genric_response()

    def solve(self):
        try:
            original_std = sys.stdout
            sys.stdout = open('open.txt', 'w')
            exec(self.code_content)
            sys.stdout.close()
            sys.stdout = original_std

            self.output_std = open('open.txt', 'r').read()
        except Exception as e:
            sys.stdout = original_std
            self.output_std = e
