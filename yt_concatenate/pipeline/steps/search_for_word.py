from .step import Step
from yt_concatenate.model.found import Found
from pprint import pprint

class SearchForWord(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue

            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)

        print(f'在此頻道找到 {len(found)} 次關鍵字')
        # print(f'found {search_word} in {found}')
        # pprint(found)
        return found
