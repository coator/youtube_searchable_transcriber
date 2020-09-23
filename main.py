import os
import argparse


def textfile():
    parser = argparse.ArgumentParser('location of text file')
    parser.add_argument('--fn', type=str)
    args = parser.parse_args()
    return args.fn


def optionfile(parser_result):
    filelocation = os.getcwd() + '/' + parser_result
    filetext = str()
    with open(filelocation, 'r') as f:
        for linenum, line in enumerate(f):
            if linenum % 2 == 1:
                pass
            else:
                filetext = filetext + ' ' + line
    return filetext


def returnfile(filetext):
    filetext = filetext.replace('\n', '')
    with open('returnfile.txt', 'w') as f:
            f.write(filetext)
    f.close()


fileloc = textfile()
textdoc = optionfile(fileloc)
returnfile(textdoc)