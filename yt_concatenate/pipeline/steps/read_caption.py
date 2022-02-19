# standard library imports
import json
from pprint import pprint

# related third party imports

# local application/library specific imports
from yt_concatenate.pipeline.steps.step import Step
from yt_concatenate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:

            if not utils.caption_file_exists(yt):
                continue

            captions = {}
            with open(yt.caption_filepath, 'r', encoding='UTF-8') as f:

                for line in f:
                    line = line.strip()                     # strip()：去除 換行、空白 等符號
                    line = json.loads(line)                 # 原來字典儲存的物件是 json，因此需要把 json 反解碼後才可以讀取。要 json.loads(),才能把 json 格式轉為 python 識別的格式。 TypeError: string indices must be integers, ref:https://www.gushiciku.cn/pl/pn0M/zh-tw

                    # 取得字幕
                    caption_line = line['text']

                    # 取得時間
                    time_line_start = round(line['start'], 4)                           # 取得 開始時間
                    time_line_duration = round(line['duration'], 4)                     # 取得 持續時間
                    time_line_end = round(time_line_start + time_line_duration, 4)      # 結束 = 開始 + 持續
                    # time_line = str(time_line_start) + ' --> ' + str(time_line_end)     # srt 格式
                    time_line = str(time_line_start), str(time_line_end)

                    # 我寫的 用於測試 edit_video.py
                    # print(time_line)
                    # # print(type(time_line))
                    # print(time_line[0])
                    #
                    # def parse_caption_time(caption_time):
                    #     start = caption_time[0]
                    #     end = caption_time[1]
                    #     return start, end
                    #
                    # def parse_time_str(time_str):
                    #     intergers, ms = str(time_str).split('.')
                    #     # intergers, ms = time_line[0].split('.')
                    #     h = int(intergers) // 3600
                    #     m = int(intergers) // 60
                    #     s = str(round(int(intergers) / 60, 2)).split('.')[-1]
                    #     ms = ms[:2]
                    #     sec = float(s + "." + ms)
                    #
                    #     print(f'hr:{h}, min:{m}, sec:{sec}')
                    #     return h, m, sec
                    #
                    # a = parse_time_str(time_line_start)
                    # b = parse_time_str(time_line_end)
                    # print(a)
                    # print(b)
                    # print('')
                    ##############

                    captions[caption_line] = time_line

                    '''
                    # captions = {line['text'], line['start']}   # captions = {text: start_time}
                    end_time = int(line['start']) + int(line["duration"])
                    captions[line['text']] = line['start'], end_time
                    # captions = {line['start'], line['text']}
                    '''

                    # print('new_caption', captions)
                # data[caption_file] = captions

            yt.captions = captions
            # pprint(data)
        return data

