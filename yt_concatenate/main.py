from yt_concatenate.pipeline.pipeline import Pipeline
from yt_concatenate.pipeline.steps.preflight import Preflight
from yt_concatenate.pipeline.steps.get_video_list import GetVideoList
from yt_concatenate.pipeline.steps.initialize_yt import InitializeYT
from yt_concatenate.pipeline.steps.download_captions import DownloadCaptions
from yt_concatenate.pipeline.steps.read_caption import ReadCaption
from yt_concatenate.pipeline.steps.search_for_word import SearchForWord
from yt_concatenate.pipeline.steps.download_videos import DownloadVideos
from yt_concatenate.pipeline.steps.edit_video import EditVideo
from yt_concatenate.pipeline.steps.postflight import Postflight
from yt_concatenate.utilities import Utils
from yt_concatenate.pipeline.steps.step import StepException
from yt_concatenate.pipeline.steps.command_line_arguments import command_line_args

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        # 'channel_id': 'UCKSVUHI9rbbkXhvAXK-2uxA',
        # 'search_word': 'incredible',
        # 'limit': 50,
        'channel_id': '',
        'search_word': '',
        'limit': 0,
        'cleanup': False,
        'fast': False
    }
    inputs = command_line_args(inputs)
    print(inputs)

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        SearchForWord(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)                 # init 的時候
    p.run(inputs, utils)                # 執行 class Pipeline 的 def run():


if __name__ == '__main__':
    main()
