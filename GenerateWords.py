import os
import sys


def check_cn(str):
    for ch in str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def add_all(o, t):
    for s in t:
        if s != '':
            o.append(s)
    return o


try:
    my_argv = sys.argv
    words = []
    if len(my_argv) > 1:
        my_argv.pop(0)
        for argv in my_argv:
            if argv[-3:] == 'txt':
                file = open(argv, 'r')
                add_all(words,
                        file.read().encode('utf-8').decode('utf-8').replace(',', ' ').replace('\t', '\n').replace('（', '(').split('\n'))
                file.close()
    data = ''
    for word in words:
        if word == '' or word == ' ' or check_cn(word) or word == '=':
            continue
        else:
            if ' ' in word:
                now_index = word.index(' ')
                data += word[:now_index] + '\n'
            elif '=' in word:
                now_index = word.index('=')
                data += word[:now_index] + '\n'
            elif '(' in word:
                now_index = word.index('(')
                data += word[:now_index] + '\n'
            elif '/' in word:
                now_index = word.index('/')
                data += word[:now_index] + '\n'
            else:
                data += word + '\n'
    path = os.getcwd() + r'\words.txt'
    file = open(path, 'w', encoding='utf-8')
    file.write(data)
    file.close()
except Exception as e:
    print(e)
    input('发生异常，回车结束程序')
