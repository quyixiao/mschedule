# 接口不完善，在远程结点上执行这个问题
from subprocess import Popen, PIPE

proc = Popen('echo "hello world "', shell=True, stdout=PIPE)
code = proc.wait()
text = proc.stdout.read()
print(text)
