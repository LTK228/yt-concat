# standard library imports
import os
import json

# related third party imports
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

# local application/library specific imports
from .step import Step
from .step import StepException
from yt_concatenate.settings import YOUTUBES_URL_DIR


class DownloadCaptions(Step):  # 1. 繼承 Step 抽象類別
    def process(self, data, inputs, utils):  # 2. 覆寫 抽象方法

        # 我寫的：以 頻道 id 當作檔案名，並優先讀取此檔案的下載連結檔案。
        channel_id = inputs['CHANNEL_ID']
        yt_urls = open(os.path.join(YOUTUBES_URL_DIR, channel_id + '.txt'), 'r', encoding='utf-8')
        ########

        # for url in data:
        for url in yt_urls:
            # print(url, end='')

            video_id = url.split('watch?v=')[-1]
            # print(video_id, end='')

            if utils.caption_file_exist(url):               # 如果字幕檔案已存在， 1.印出消息、2.跳過下載。
                print('found existing caption file', video_id.replace("\n", "") + ".txt")
                continue

            try:
                captions = YouTubeTranscriptApi.get_transcript(video_id)
                captions_l = list(json.dumps(i) for i in captions)

                # 我寫的：把字幕檔案寫在 downloads/captions 裡面
                self.save_caption_to_file(captions_l, utils.get_caption_path(url))

            except Exception:
                # pass                              # 如果這個字幕檔無法下載而發生錯誤，就跳過他，繼續下載其他的。
                continue                                  # 如果這個字幕檔無法下載而發生錯誤，就跳過他，繼續下載其他的。

        yt_urls.close()
        # print(data)
        return data

    # 我寫的：把字幕檔案寫在 downloads/captions 裡面
    def save_caption_to_file(self, captions_l, filepath):
        with open(filepath, "w", encoding='UTF-8') as fp:
            print(f'新增檔案：路徑位於 {filepath}')
            for subtitle in captions_l:
                fp.write(subtitle + '\n')
