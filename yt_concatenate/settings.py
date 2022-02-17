from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

DOWNLOAD_DIR = 'downloads'
YOUTUBES_URL_DIR = os.path.join(DOWNLOAD_DIR, 'video_url')
VIDEOS_DIR = os.path.join(DOWNLOAD_DIR, 'videos')
CAPTIONS_DIR = os.path.join(DOWNLOAD_DIR, 'captions')

