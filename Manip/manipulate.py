import os
from PyPDF2 import PdfFileReader
from Objects.pdf import *
from Objects.keyword import *
from Manip.statistics import prioratize


files = [
    [],  # files as str
    [],  # files as objects
]
keywords = [
    Keyword('word'),
    Keyword('keyword'),
    Keyword('find'),
    Keyword('search'),
    Keyword('Git')
]  # list of Keyword Objects

results = [] # result files from word matching

dbg_path = '/home/zlat/Downloads'  # debugging path
user_path = None
path = ''


def find_pdf(fpath, name):
    """
    find a specific file (name) in a specific dir (path)
    if found append in the files list
    :param path: path to search for pdf files
    :param name: name of the file to find
    :return: None
    """
    for file in os.listdir(fpath):
        if file.endswith('.pdf'):
            flag = re.search(name, file)
            if flag:
                files.append(file)
    if files:
        print('Found file in ' + fpath)
    else:
        print('Could not find files in ' + fpath)


def find_pdf_all(fpath):
    """
    mostly used
    enter a path and append all pdf files in the files list
    :param path: path to find pdf files
    :return: None
    """
    for file in os.listdir(fpath):
        if file.endswith('.pdf'):
            files[0].append(file)

    if files[0]:
        print('Found files in ' + fpath)
    else:
        print('Could not find pdf files in ' + fpath)


def find_every_file():
    """
    not working yet
    search every directory in the linux's home folder
    append all files found in the files list
    :return: None
    """
    pass
    status = False
    for file in os.listdir('/home/'):
        if file.endswith('.pdf '):
            files.append(file)
            status = True

    if status:
        print('Found pdf files in ' + path)
    else:
        print('Could not found pdf files in ' + path)


def print_results(verbose=False):
    """
    prints results from the search
    :param verbose: if True print files with some extra info
    :return: None
    """
    for i in files:
        print(i)

    if verbose:
        print('Name\tPages')
        for file in files[1]:
            print(file.name + '\t' + file.pages)


def open_pdfs():

    if not files:
        return False

    # for i in range(files.__len__()):
    #     print(files[i])
    #     pdf_files.append(PDF(files[i]))
    #
    #     open_file = open(path + files[i], 'rb')
    #     pdf_open_file = PdfFileReader(open_file, strict=False)
    #
    #     for page in range(pdf_open_file.getNumPages()):
    #         content = pdf_open_file.getPage(page)
    #         pdf_files[i].text += content.extractText()
    #
    #     open_file.close()

    for file in files[0]:
        print(file)
        files[1].append(PDF(file))

        open_file = open(path + file, 'rb')
        pdf_open_file = PdfFileReader(open_file, strict=False)

        for page in range(pdf_open_file.getNumPages()):
            content = pdf_open_file.getPage(page)
            files[1][-1].text += content.extractText()


def match_keywords():

    # for pdf in files[1]:
    #     for word in keywords:
    #         found = re.findall(word.name, pdf.text)
    #         if found:
    #             print(found)
    #             word.file_appeared[pdf.title] = found.__len__()
    #             print(word.file_appeared)
    #             print(files[0])
    #     results.append(files[0])
    # print(results)

    for i in range(files[1].__len__()):
        for word in keywords:
            found = re.findall(word.name, files[1][i].text)
            if found:
                print(found)
                word.file_appeared[files[0][i]] = found.__len__()
                print(word.file_appeared)
        results.append(files[0][i])
    print(results)




def return_result(result_index, verbose=False):

    return results[result_index]


def get_path():
    new = input('Select path: /home/')
    if new.endswith('/'):
        final_new = '/home/' + new
    else:
        final_new = '/home/' + new + '/'

    return final_new


def extract_s_text(content, field, chapter = 0):
    """
    extract specific text from a text content
    used for scientific papers
    can be used to extract abstract or a specific chapter
    :param content: the entire text to search, in this caase the pdf content
    :param field: the field of the file to search like abstract or keywords
    :param chapter: a numbered chapter of the file (default 0)
    :return:None
    """


if __name__ == '__main__':
    path = '/home/zlat/Downloads/'
    find_pdf_all(path)
    open_pdfs()
    match_keywords()
    prioratize()