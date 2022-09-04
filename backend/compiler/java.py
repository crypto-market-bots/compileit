import subprocess
import uuid

from numpy import delete
from compiler.cpp import *

def compile_code_java(code_source):
    file_code = "../tmp/"+str(uuid.uuid4())
    save_code(file_code, ".java", code_source)

    s = subprocess.check_output("javac HelloWorld.java;java HelloWorld", shell = True)
    delete_files(file_code, ".java")
    return s.decode('utf-8')