# standard library imports
import os
# related third party imports
from dotenv import load_dotenv

load_dotenv()                   # take environment variables from .env.
# load_dotenv(verbose=True)       # 其他模式：印出詳細資訊 (載入哪些資料)
API_KEY = os.getenv('API_KEY')

DOWNLOADS_DIR = 'downloads'
YOUTUBES_URL_DIR = os.path.join(DOWNLOADS_DIR, 'video_url')
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
