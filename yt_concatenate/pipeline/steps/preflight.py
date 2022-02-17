from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Preflight')
        print('Creating the necessary folders!')
        print('')
        utils.create_dirs()
