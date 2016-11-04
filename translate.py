# coding: utf-8

import requests

url_trans = u'http://fanyi.baidu.com/v2transapi'


def cht_zh(text):
    data = {
        u'from': u'cht',
        u'to': u'zh',
        u'query': text,
        u'transtype': u'translang',
        u'simple_means_flag': 3
    }
    response = requests.post(url_trans, data=data)
    try:
        result = response.json().get(u'trans_result').get(u'data')[0].get(u'dst')
        print(result)
        return result
    except AttributeError as err:
        print(err)
    return text

if __name__ == '__main__':
    result =cht_zh(u'歷史通常是由胜利者所写的')
    # print(result)
