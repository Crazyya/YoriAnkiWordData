import os

from lxml import etree
import sys

import requests

base_url = 'https://www.youdao.com/w/{keyword}'


def err_fun(msg):
    print(msg)


def get_html(keyword):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/65.0.3325.181 Safari/537.36 '
        }
        r = requests.get(base_url.format(keyword=keyword), timeout=30, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return get_html_data(r.text)
        else:
            err_fun(r.text)
    except Exception as e:
        err_fun('{keyword}获得html异常：{e_msg}'.format(keyword=keyword, e_msg=str(e)))


def get_html_data(html_text):
    result = {}
    page = etree.HTML(html_text)
    keyword = page.xpath(u'//*[@id="phrsListTab"]/h2/span[@class="keyword"]/text()')[0]
    try:
        phonetic = page.xpath(u'//*[@id="phrsListTab"]/h2/div/span[1]/span[@class="phonetic"]/text()')[0]
    except:
        try:
            phonetic = page.xpath(u'//*[@id="phrsListTab"]/h2/div/span[2]/span[@class="phonetic"]/text()')[0]
        except:
            phonetic = ''
    trans_containers = page.xpath(u'//*[@id="phrsListTab"]/div[2]/ul/li/text()')
    translations_en = page.xpath(u'string(//*[@id="bilingual"]/ul/li[1]/p[1])')
    translations_zh = page.xpath(u'string(//*[@id="bilingual"]/ul/li[1]/p[2])')
    paraphrases = ''
    for paraphrase in trans_containers:
        paraphrases += paraphrase + '\n'
    paraphrases = paraphrases[:-2]
    translation = translations_en.replace('\n', '').replace('\t', '').strip() + '\n' + translations_zh.replace('\n',
                                                                                                               '').replace(
        '\t', '').strip()
    result["keyword"] = str(keyword)
    result["phonetic"] = str(phonetic)
    result["paraphrases"] = str(paraphrases)
    result["translation"] = str(translation)
    return result


def add_all(o, t):
    for s in t:
        if s != '':
            o.append(s)
    return o


try:
    keywords = []
    my_argv = sys.argv
    if len(my_argv) > 1:
        my_argv.pop(0)
        for argv in my_argv:
            if argv[-3:] == 'txt':
                file = open(argv, 'r')
                add_all(keywords,
                        file.read().encode('utf-8').decode('utf-8').replace(',', '\n').replace(' ', '\n').replace(';', '\n').replace('，', '\n').split(
                            '\n'))
                file.close()
    else:
        keywords.append(input('输入生成的单词：'))
    print('获得{count}个单词准备获取'.format(count=len(keywords)))
    datas = []
    for keyword in keywords:
        data = get_html(keyword)
        if data is not None:
            datas.append(data)
            print('{keyword}获取完成'.format(keyword=keyword))
    print('网络数据获取完成，写入txt')
    msg = ''
    for data in datas:
        msg += '{a}\t{b}\t"{c}"\t"{d}"\n'.format(a=data["keyword"], b=data["phonetic"], c=data["paraphrases"],
                                                 d=data["translation"])
    file = open(os.getcwd() + '/data.txt', 'w', encoding='utf-8')
    file.write(msg)
    file.close()
    input('程序执行完毕，回车结束')
except Exception as e:
    input('异常信息:{e}'.format(e=str(e)))
