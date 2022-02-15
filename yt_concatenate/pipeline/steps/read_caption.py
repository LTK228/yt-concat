# standard library imports
import os
import json
from pprint import pprint

# related third party imports

# local application/library specific imports
from .step import Step
from .step import StepException
from yt_concatenate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}

        # print(os.listdir(CAPTIONS_DIR))
        for caption_file in os.listdir(CAPTIONS_DIR):       # os.listdir()：把資料夾內的內容，都列出來 (list)
            captions = {}
            print(os.path.join(CAPTIONS_DIR, caption_file))

            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r', encoding='UTF-8') as f:
            #     print(f, end="")

                for line in f:
                    line = line.strip()                     # strip()：去除 換行、空白 等符號
                    line = json.loads(line)                 # 原來字典儲存的物件是 json，因此需要把 json 反解碼後才可以讀取。要 json.loads(),才能把 json 格式轉為 python 識別的格式。 TypeError: string indices must be integers, ref:https://www.gushiciku.cn/pl/pn0M/zh-tw
                    # print(line, end="")
                    # print(type(line), end="")

                    # 取得字幕
                    caption_line = line['text']             # 取得字幕
                    # print(caption_line)

                    # 取得時間
                    time_line_start = round(line['start'], 3)                           # 取得 開始時間
                    time_line_duration = round(line['duration'], 3)                     # 取得 持續時間
                    time_line_end = round(time_line_start + time_line_duration, 3)      # 結束 = 開始 + 持續
                    time_line = str(time_line_start) + ' --> ' + str(time_line_end)     # srt 格式

                    # print(type(time_line_start), end="")
                    # print(time_line_duration, end="")
                    # print(time_line_end)
                    # print(f'{time_line_start} --> ', end="")
                    # print(time_line)

                    captions[caption_line] = time_line      # 存入字典： key:value = caption:time
                # print(captions)
                # pprint(captions)

            data[caption_file] = captions                   # 存入字典： key:value = filename: {caption:time}
            # print(data)
            # pprint(data)
            break                                           # 只跑一個字幕檔
        return data
