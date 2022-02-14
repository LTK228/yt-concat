from .steps.step import StepException               # 相對路徑寫法


class Pipeline:
    def __init__(self, steps):                      # property：裝載著步驟 (steps) 的清單
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:                     # 將上面的 property 都跑過一遍
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print('Exception happened', e)
                break                               # 只要出錯，跳出迴圈！
