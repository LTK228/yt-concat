# standard library imports
import os
import json
import time

# related third party imports
from youtube_transcript_api import YouTubeTranscriptApi

# local application/library specific imports
from .step import Step
from .step import StepException
from yt_concatenate.settings import VIDEOS_DIR
from yt_concatenate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):                   # 1. 繼承 Step 抽象類別
    def process(self, data, inputs, utils):     # 2. 覆寫 抽象方法
        start = time.time()

        for yt in data:
            if utils.caption_file_exists(yt):
                print(f'found existing caption file {yt.id}.txt')
                continue

            video_id = yt.url.split('watch?v=')[-1]

            try:
                captions = YouTubeTranscriptApi.get_transcript(video_id)
                captions_l = list(json.dumps(i) for i in captions)

                with open(os.path.join(CAPTIONS_DIR, video_id.replace("\n", "") + ".txt"), "w", encoding='UTF-8') as fp:
                    for i in captions_l:
                        fp.write(i + '\n')

            except Exception:
                pass                            # 如果這個英文字幕檔無法下載，就跳過他，繼續下載其他的。
                # continue
                # raise StepException
        end = time.time()
        print('took', round(end - start, 4), 'seconds')
        return data
