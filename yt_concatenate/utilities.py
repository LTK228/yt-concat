# 主要寫 helper function

# standard library imports
import os

# related third party imports

# local application/library specific imports
from yt_concatenate.settings import DOWNLOADS_DIR
from yt_concatenate.settings import YOUTUBES_URL_DIR
from yt_concatenate.settings import VIDEOS_DIR
from yt_concatenate.settings import CAPTIONS_DIR


def get_video_list_filepath(channel_id):
    return os.path.join(YOUTUBES_URL_DIR, channel_id + '.txt')


class Utils:
    def __init__(self):
        pass

    # preflight.py
    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(YOUTUBES_URL_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)

    # get_video_list.py
    @staticmethod
    def video_list_file_exists(self, channel_id):
        path = get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0  # 1. 檢查路徑、 2. 如果檔案大小 > 0 (有可能還沒存到內容，只建立了空檔案，就當了)

    @staticmethod
    def get_video_id_from_url(url):
        return url.split('watch?v=')[-1]

    # download_captions.py
    def get_caption_path(self, url):
        # print(os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url)).replace("\n", "") + ".txt")
        return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url).replace("\n", "") + ".txt")
        # return os.path.join(CAPTIONS_DIR, self.get_video_id_from_url(url) + ".txt")

    def caption_file_exist(self, url):
        path = self.get_caption_path(url)
        return os.path.exists(path) and os.path.getsize(path) > 0  # 1. 檢查路徑、 2. 如果檔案大小 > 0 (有可能還沒存到內容，只建立了空檔案，就當了)

