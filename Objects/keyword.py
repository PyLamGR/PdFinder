# Stylianos Zlatintsis
# date: 2/3/18

import re


class Keyword:
    def __init__(self, name):
        """
        class Keyword holds info about a keyword being searched in a pdf file
        :param name: holds the keyword
        """
        self.name = name
        # self.length = len(name)
        # self.ignored()
        self.file_appeared = {}  # file name : times appeared
        self.ignore = False
        self.ignored()

    def appeared(self, file):
        """

        :return: None
        """
        if not self.ignored():
            # appearance = 1
            pass

    def ignored(self):
        # check if a keyword is ignorable
            if len(self.name) <= 3:
                self.ignore = True

    def is_derivative(self, word):
        # special function to check i a keyword is part from another word
        return re.findall(self.name, word, re.I)

    def print_key(self):
        print('Word :' + self.name)
        print('Length: ' + str(len(self.name)))
        print('Ignorable: ' + str(self.ignore))


def get_keyword():
    keyword = input('Enter keyword: ')
    keyword = Keyword(keyword)
    keyword.ignored()


if __name__ == '__main__':
    new_word = Keyword("name")
    new_word.appearance = len(new_word.is_derivative('surname name is my name'))
    print(new_word.appearance)
    new_word.print_key()
