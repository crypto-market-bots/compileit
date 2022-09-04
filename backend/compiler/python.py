import subprocess
from unittest import result
import uuid
from compiler import cpp


def compile_code_python(code_source, stdin):
    file_code = '/tmp/'+str(uuid.uuid4())
    cpp.save_code(file_code, '.py', code_source)

    file_path = file_code + ".py"

    cmd = ["python3 "+file_path]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                         shell=True, stderr=subprocess.STDOUT)
    if stdin != '':
        p.communicate(stdin)
    # delete_files(file_code)
    p.wait()
    result = p.stderr if p.stderr != None else p.stdout.read()

    if p.stderr == None:
        print(result)
    container = str(result).replace(file_code+".py", '')
    if p.stderr:
        container.pop(0)

    cpp.delete_files(file_code, ".py")
    return result.decode('utf-8')
