# 接口不完善，在远程结点上执行这个问题
import socket
from subprocess import Popen, PIPE

from agent.executor import Executor
from agent.msg import Message

proc = Popen('echo "hello world "', shell=True, stdout=PIPE)
code = proc.wait()
text = proc.stdout.read()
print(text)




exec = Executor()
print(exec.run('echo "1111111"'))
message = Message('/Users/quyixiao/PycharmProjects/mschedule/logs/myid')

print(message.get_addresses())
print(socket.gethostname())