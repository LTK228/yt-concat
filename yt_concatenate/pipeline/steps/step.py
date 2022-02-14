from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def process(self, data, inputs, utils):
        pass


class StepException(Exception):
    """
    目的是當執行裡面的 step 的時候，
    任何一個步驟有觸發，我們設計的 StepException，
    就停止執行，因執行後續沒有意義。
    e.g. 下載不到 YouTube 的影片。
    """
    pass

