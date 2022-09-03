from subprocess import check_output, STDOUT, CalledProcessError
import subprocess
from subprocess import STDOUT,PIPE
import os
import uuid

def save_code(file_code, extension, code_source):
    f = open(file_code+extension, 'w+')
    f.write(code_source)
    
def delete_files(file_code, ext):
    try:
        os.remove(file_code+ext)
        os.remove(file_code+".txt")
    except:
        return 

def check_error(file_code):
    error_file = file_code
    with open(error_file) as f:
        lines = f.readlines()
    return "".join(lines)

def compile_code_cpp(code_source, stdin):
    file_code = "../tmp/"+str(uuid.uuid4())
    save_code(file_code, ".cpp", code_source)

    file_path = file_code + ".cpp"
    
    try:
        cmd = "g++ "+ file_path +" &> "+file_code+".txt"
        #tmp=subprocess.call(["./a.out"]) 
        p = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True)
        p.wait()
        error = check_error(file_code+".txt")
        if error != "":
            delete_files(file_code, ".cpp")
            return error

        cmd = ['./a.out']
        proc = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        if stdin != '':
            proc.communicate(stdin)
        delete_files(file_code, ".cpp")
        return proc.stderr if proc.stderr != None else proc.stdout.read() 

    except Exception as e:
        delete_files(file_code, ".cpp")
        return "something went wrong ! please try again"