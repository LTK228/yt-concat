# standard library imports
import os
from time import time
from math import ceil
from threading import Thread
from multiprocessing import Process

# related third party imports
from pytube import YouTube  # pip install --upgrade pytube

# local application/library specific imports
from .step import Step
from yt_concatenate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):         # 上一步驟 Search return 的資料為 found 字典，在此會作為 data 傳入。
        """
        使用 multi-threading 需要先將 urls 拆成不同群組，避免 thread 互相影響。
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
        # print(len(data))
        yt_set = set([found.yt for found in data])  # 利用 set 功能去除重複的 yt 清單，避免重複下載影片。
        print('videos to download=', len(yt_set))

        yt_set = list(yt_set)
        # self.use_pytube_download_video(yt_set, utils)   # 一般下載模式 (未使用 multi-threading)。

        ##############
        # # Multi-threading
        start = time()

        chunk = ceil(len(yt_set) / os.cpu_count())

        group = []
        for i in range(0, len(yt_set), chunk):
            group.append(yt_set[i: i + chunk])
        # print(group)
        # print(len(group[0]))
        # print(len(group[-1]))
        # print(len(group))

        try:
            threads = []
            for i in range(os.cpu_count()):
                threads.append(Thread(target=self.use_pytube_download_video, args=(group[i], utils)))
                threads[i].start()

            for i in threads:
                i.join()
        except IndexError:
            pass

        end = time()
        print(f'---------------Multi-threading download elapsed time= {end - start} seconds')
        #############

        return data

    def use_pytube_download_video(self, yt_set, utils):
        for yt in yt_set:

            url = yt.url
            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            print('downloading', url)
            YouTube(url).streams.filter(res="360p").first().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
