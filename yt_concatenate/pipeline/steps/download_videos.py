# standard library imports
from __future__ import unicode_literals

import os
from time import time

# related third party imports
from youtube_dl import YoutubeDL

# local application/library specific imports
from .step import Step
from yt_concatenate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        # print(len(data))

        yt_set = set([found.yt for found in data])          # 將重複的連結，利用 set 來去除重複的。
        # print(len(yt_set))
        print(f'videos to download = {len(yt_set)}')
        print('')

        # for found in data:
        # yt = found.yt
        time_start = time()

        for yt in yt_set:
            url = yt.url
            path = os.path.join(VIDEOS_DIR, yt.id + '.mp4')
            # print(url)
            # print(path)

            if utils.video_file_exists(yt):                 # 如果影片已經存在，就不再下載
                print(f'found existing video file for {url}, skipping.')
                print('')
                continue

            try:
                print(f'Will be download of the {url}')

                # 我寫的：透過 youtube_dl 下載影片 #######
                # youtube_id operations，youtube_id 的各項屬性，可以根據你的需求加減
                ydl_opts = {
                    'format': 'worst',      # 畫質：最差 (防止主機炸裂)
                    'outtmpl': path,        # 輸出路徑
                }

                YoutubeDL(ydl_opts).download([url])
                print(f'Complete the download of the {yt.id}.mp4')
                print('')
                #################

                # YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)     # PyTube 無法使用

            except Exception as e:         # YouTube(url).streams.first() 發生的錯誤
                print(f'happened error: {e}')
                print(f"An Error occur for {yt.id}.mp4")
                print('')
                continue                                    # 發生錯誤的影片，跳過下載。

        time_end = time()
        time_c = time_end - time_start
        print(f'time cost {time_c} sec')

        return data
