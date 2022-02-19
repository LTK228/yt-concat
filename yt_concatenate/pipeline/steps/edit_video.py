# standard library imports

# related third party imports
from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

# local application/library specific imports
from .step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            # print(f'found.time: {found.time}')
            # print(self.parse_caption_time(found.time))
            start, end = self.parse_caption_time(found.time)
            print('')

            # 我寫的：如果檔案已存在，不再執行合併影片。
            # if utils.output_file_exists(inputs['channel_id'], inputs['search_word']):
            #     print(f"found existing caption file {inputs['channel_id']}_{inputs['search_word']}.mp4")
            #     return

            # 我寫的：影片尚未齊全，若沒找到影片就先跳過
            # print(found.yt.video_filepath)
            if not utils.video_file_exists(found.yt):
                continue
            ###

            video = VideoFileClip(found.yt.video_filepath).subclip(start, end)

            clips.append(video)
            if len(clips) >= inputs['limit']:       # 如果影片裝超過限制數，就停止下載，避免 RAM 超載。
                break

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, caption_time):
        start = caption_time[0]
        end = caption_time[1]
        return self.parse_time_str(start), self.parse_time_str(end)

    def parse_time_str(self, time_str):
        interger, ms = str(time_str).split('.')

        h = int(interger) // 3600

        interger = int(interger) - (h * 3600)
        m = int(interger) // 60

        s = str(int(interger) - (m * 60))
        if len(s) < 2:      # 如果 sec 的最末位是 0，int 型態會被消失，所以如果沒有就補上 0。
            s = '0' + s

        ms = ms[:2]
        sec = float(f'{s}.{ms}')

        return h, m, sec
