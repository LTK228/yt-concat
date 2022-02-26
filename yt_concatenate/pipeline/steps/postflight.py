from .step import Step

class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')
        print('Videos and captions are being deleted')
        print('during the processing of the composite video')
        print('')
        if inputs['cleanup']:
            utils.remove_dirs()
