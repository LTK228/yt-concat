# standard library imports
import os
import json
from time import time
from math import ceil
from threading import Thread

# related third party imports
from youtube_transcript_api import YouTubeTranscriptApi

# local application/library specific imports
from .step import Step
from .step import StepException
from yt_concatenate.settings import VIDEOS_DIR
from yt_concatenate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):  # 1. 繼承 Step 抽象類別
    def process(self, data, inputs, utils):  # 2. 覆寫 抽象方法
        """
        1. 將 yt_set 的 url，拆成小群組。
            chunk = ceil(len(yt_set) / os.cpu_count)

        2. 一次要取 chunk 的數量，才能分成群組
            group = []
            for i in range(0, len(yt_set), chunk):
                group.append(yt_set[i: i+chunk])

        3. 裝到 threads 裡面，分 os.cpu_count() 次裝入
            threads = []
            for i in range(os.cpu_count()):
                threads.append(group[i])
        """
        ##############
        # # Multi-threading
        start = time()

        chunk_size = ceil(len(data) / os.cpu_count())

        group = []
        for i in range(0, len(data), chunk_size):
            group.append(data[i: i + chunk_size])

        try:
            threads = []
            for i in range(os.cpu_count()):
                t = Thread(target=self.dowload_caption, args=(group[i], utils))
                threads.append(t)
                threads[i].start()

            for i in threads:
                i.join()
        except IndexError:
            pass

        end = time()
        print(f'-----Multi-threading download captions elapsed time= {end - start} seconds-----')
        return data

    def dowload_caption(self, group, utils):
        for yt in group:
            if utils.caption_file_exists(yt):
                # print(f'found existing caption file {yt.id}.txt')
                continue

            video_id = yt.url.split('watch?v=')[-1]

            try:
                captions = YouTubeTranscriptApi.get_transcript(video_id)
                captions_l = list(json.dumps(i) for i in captions)

                filepath = os.path.join(CAPTIONS_DIR, video_id.replace("\n", "") + ".txt")
                with open(filepath, "w", encoding='UTF-8') as fp:
                    print(f'新增檔案：路徑位於 {filepath}')
                    for i in captions_l:
                        fp.write(i + '\n')

            except Exception:
                pass  # 如果這個英文字幕檔無法下載，就跳過他，繼續下載其他的。
                # continue
                # raise StepException
