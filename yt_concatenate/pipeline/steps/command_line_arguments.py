import sys
import getopt



def print_usage():
    # print('python sys_args.py -u <username> -p <password>')
    # print('python sys_args.py --username <username> --password <password>')

    print('python -m yt_concatenate.main OPTIONS')
    print('')
    print('OPTIONS:')
    print('  The following must be entered')
    print('{:>6} {:<20} {}'.format('-c', '--channel', 'Channel id of the Youtube channel to download'))
    print('{:>6} {:<20} {}'.format('-s', '--searchword', 'Key word to look for in the channel'))
    print('{:>6} {:<20} {}'.format('-l', '--limit', 'Limit the number of movies needed for edit movie'))
    print('')
    print('  The following is optional')
    print('{:>6} {:<20} {}'.format('', '--cleanup', 'Remove captions and videos download during run'))
    print('{:>6} {:<20} {}'.format('-f', '--fast', 'Activate fast-forward mode, if you have already'))
    print('{:>6} {:<20} {}'.format('', '', 'downloaded caption or videos, do not download them again.'))


def command_line_args(inputs):
    """
    Search: python command line arguments
    https://www.tutorialspoint.com/python/python_command_line_arguments.htm

    short opts 後面有冒號代表要接參數，例如 i: 、 o: 就要要參數、h 不用。
    long opts 後面有等號代表要接參數，例如 ifile=
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    """

    short_opts = 'hu:p:c:s:l:f'                        # : 代表後面要參數
    long_opts = 'help username= password= channel= searchword= limit= cleanup fast'.split()  # = 代表要參數

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)  # argv[1:] 一定要記得
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    # print(f'opts is {opts}')
    # print(f'opts is {len(opts)}')
    # print(f'args is {args}')


    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_usage()
            sys.exit(0)                     # 使用 help 後，就正常結束。
        elif opt in ("-c" ,'--channel'):
            inputs['channel_id'] = arg
        elif opt in ("-s", '--searchword'):
            inputs['search_word'] = arg
        elif opt in ("-l", '--limit'):
            inputs['limit'] = arg
        elif opt == '--cleanup':
            inputs['cleanup'] = True
        elif opt in ('-f', '--fast'):
            inputs['fast'] = True

    # check 1: The following must be entered
    if not (inputs['channel_id'] and inputs['search_word'] and inputs['limit']):
        print_usage()
        sys.exit(2)

    # check 2
    if len(opts) < 3:
        print_usage()
        sys.exit(2)

    return inputs
