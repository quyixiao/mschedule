from subprocess import Popen, PIPE

from utils import getlogger

logger = getlogger(__name__, '/Users/quyixiao/ttg/test.log')  # 路径自行更换


class Executor:
    def __init__(self, script, timeout=None):
        self.script = script
        self.timeout = timeout

    def run(self):
        proc = Popen(self.script, shell=True, stdout=PIPE)
        code = proc.wait(self.timeout)
        text = proc.stdout.read()
        logger.info(str(code) + ' ' + str(text))
        return code, text


exec = Executor('echo "1111111"')
print(exec.run())
