from unittest import result
from cpp import *

def compile_code_python(code_source, stdin):
    file_code = "../tmp/"+str(uuid.uuid4())
    save_code(file_code, ".py", code_source)

    file_path = file_code + ".py"

    cmd = ["python3 "+file_path]
    p = subprocess.Popen(cmd,stdout=subprocess.PIPE, shell=True, stderr=STDOUT)
    if stdin != '':
        p.communicate(stdin)
    #delete_files(file_code)
    p.wait()
    result = p.stderr if p.stderr != None else p.stdout.read() 
    delete_files(file_code, ".py")
    return result