import zerorpc
import threading
from .config import CONNECTIONURL
from utils import getlogger
from .msg import Message
from .state import *
from .executor import Executor

logger = getlogger(__name__, '/Users/quyixiao/PycharmProjects/mschedule/logs/agent.cm.log')


class ConnectionManager:
    def __init__(self):
        self.client = zerorpc.Client()
        self.message = Message('/Users/quyixiao/PycharmProjects/mschedule/logs/myid')
        self.event = threading.Event()
        self.state = WAITING # 当任务完成了
        self.exec = Executor()

    def start(self, timeout=5):
        try:
            self.event.clear() # 重置event
            self.client.connect(CONNECTIONURL) # 建立连接
            logger.info(self.client.sendmsg(self.message.reg()))

            # 心跳循环
            while not self.event.wait(timeout):
                logger.info(self.client.sendmsg(self.message.heartbeat()))

                if self.state == WAITING:
                    task = self.client.get_task(self.message.id)
                    if task:
                        self.state = RUNNING
                        # [task.id, task.script, task.timeout]
                        code ,output = self.exec.run(task[1], task[2]) # 阻塞
                        self.client.sendmsg(self.message.result(task[0], code, output))
                        self.state = WAITING

        except Exception as e:
            logger.error("{}".format(e))
            raise e

    def shutdown(self):
        self.event.set()
        self.client.close()



