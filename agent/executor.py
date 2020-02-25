from subprocess import Popen, PIPE
from utils import getlogger


logger = getlogger(__name__, '/Users/quyixiao/PycharmProjects/mschedule/logs/exec.log')

class Executor:
    def run(self, script, timeout=None):
        proc = Popen(script, shell=True, stdout=PIPE)
        code = proc.wait(timeout)
        txt = proc.stdout.read()

        logger.info("{} {}".format(code, txt))
        return code,txt

