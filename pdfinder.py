
from sys import exit, argv
import argparse
from Manip.manipulate import *
from Objects.pdf import *
from GUI.gui import Root
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('keyword', help="keyword to seek", type=str)
    # parser.add_argument('-K', '--keyword', help="enter keyword as an argument int the terminal", action="count")
    parser.add_argument('-v', '--verbose', help="print results with more details", action="store_true")
    parser.add_argument('-s', '--statistics', help='print statistics of the search', action='store_true')
    # parser.add_argument('-g', '--graphical', help='show graphical environment', action='store_true')
    parser.add_argument('-c', '--current', help='search in current directory', action='store_true')
    parser.add_argument('-d', '--debug', help='use debugging path', action='store_true')
    args = parser.parse_args()

    # if args.keyword:
    #     key = Keyword(args.keyword)

    app = QApplication(argv)
    r = Root()
    exit(app.exec_())

    path = '/home'  # set home as default path

    if args.current:
        path = os.getcwd()
    elif args.debug:
        path = '/home/zlat/examples'
    else:
        if not args.graphical:
            path = get_path()

    if args.verbose:
        if not files[1]:
            print('No results')
        else:
            print_results(True)
    else:
        if not files[1]:
            print('No results')
        else:
            print_results()
