"""
這個檔案主要是寫 helper function，
2 個以上檔案需要用到的「功能」，
都寫成 function，放在這裡。
"""

# standard library imports
import os

# related third party imports

# local application/library specific imports
from yt_concatenate.settings import DOWNLOAD_DIR
from yt_concatenate.settings import YOUTUBES_URL_DIR
from yt_concatenate.settings import VIDEOS_DIR
from yt_concatenate.settings import CAPTIONS_DIR


class Utils:
    def __init__(self):
        pass

    # preflight.py
    def create_dirs(self):
        os.makedirs(YOUTUBES_URL_DIR, exist_ok=True)
        os.makedirs(DOWNLOAD_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    # get_video_list.py
    def get_video_list_filepath(self, channel_id):
        return os.path.join(YOUTUBES_URL_DIR, channel_id + '.txt')
        # return os.path.join(DOWNLOAD_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0           # 1. 檢查路徑、 2. 如果檔案大小 > 0 (有可能還沒存到內容，只建立了空檔案，就當了)

    # download_captions.py
    def caption_file_exists(self, yt):
        filepath = yt.caption_filepath
        return os.path.exists(filepath) and os.path.getsize(filepath) > 0   # 1. 檢查路徑、 2. 如果檔案大小 > 0 (有可能還沒存到內容，只建立了空檔案，就當了)
