from .state import *

class Task:
    def __init__(self, task_id, script, targets, timeout=0, parallel=1,
                 fail_rate=0, fail_count=-1):
        self.id = task_id
        self.script = script
        self.timeout = timeout
        self.parallel = parallel
        self.fail_rate = fail_rate
        self.fail_count = fail_count
        self.state = WAITING
        self.targets = {agent_id:{'state':WAITING, 'output':""} for agent_id in targets}
        self.target_count = len(self.targets)