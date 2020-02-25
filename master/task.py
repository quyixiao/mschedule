from .state import *


class Task:
    def __init__(self, task_id, script, targets, timeout=0, parallel=1, fail_rate=0, fail_count=-1):
        self.id = task_id
        self.script = script  # 任务脚本script ,base64 编码
        self.timeout = timeout  # 超时时间timeout
        self.parallel = parallel  # 并行度parallel
        self.fail_rate = fail_rate  # 失败率fail_rate
        self.fail_count = fail_count  # 失败次数fail_count
        self.state = WAITING  # targets是跑任务的Agent的agent_id列表，可以让用户看到一个列表，勾选，1-5都是文本框填写信息即可，6 即targets列表需要从Master端获取
        self.targets = {agent_id: {'state': WAITING, 'output': ""} for agent_id in targets}
        self.target_count = len(self.targets)
