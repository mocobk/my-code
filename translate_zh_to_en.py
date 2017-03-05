import urllib.request
import urllib.parse
import json
import re


def translate(src_lang,tar_lang,query):
    # 封装post表单
    form_data = {}
    form_data["from"] = src_lang
    form_data["to"] = tar_lang
    form_data["query"] = query
    form_data["transtype"] = "translang"
    form_data["simple_means_flag"] = "3"

    data = urllib.parse.urlencode(form_data).encode("utf-8")

    url = "http://fanyi.baidu.com/v2transapi"
    response = urllib.request.urlopen(url,data)

    # response.read()得到的是一个unicode编码，所以下面使用unicode-escape反编码（没有使用json时出现）
    # html = response.read().decode("unicode-escape")

    html = response.read().decode("utf-8")
    result = json.loads(html)
    #src = result["trans_result"]["data"][0]["src"]
    dst = result["trans_result"]["data"][0]["dst"]
    print(dst)


def lang_judgement(text):
    #匹配含中文或全为数字的unicode字符
    pattern = re.compile(u"[\u4e00-\u9fa5]+|^[\u0030-\u0039]+$")
    #若匹配，match返回一个对象，不匹配返回空
    match = pattern.search(text)

    if match:
        translate("zh","en",text)
    else:
        translate("en","zh",text)

while 1:
    text = str(input("请输入要翻译的内容：\n"))
    lang_judgement(text)



