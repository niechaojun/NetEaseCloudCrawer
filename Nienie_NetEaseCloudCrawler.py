#coding=utf-8
import requests as rs
from Crypto.Cipher import AES
import base64
import json
import os
import time
'''
       Coded by nienie
'''

def Nie_get_params(PageNum,Count):
    PageNum = (PageNum-1)*20
    first_param = "{ rid: \"R_SO_4_418603077\", offset: "+str(PageNum)+", total: \"false\", limit: "+str(Count)+", csrf_token: \"\" }"
    forth_param = "0CoJUm6Qyw8W8jud"
    first_key = forth_param
    second_key ='nienienienienien'
    h_encText = AES_encrypt(first_key,first_param)
    h_encText = AES_encrypt(second_key,h_encText)
    return h_encText

def AES_encrypt(key, text):
    iv = '0102030405060708'
    pad = 16 - len(text) % 16
    text +=  pad * chr(pad)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text

def Nie_get_encSecKey():
    encSrcKey = "6469da86a183fc2fc9df65ac98f67138c8d3048d0626714fe646ecb564d4f8cd386a9c9618bb8a4f2929e50ba32e8991266aba783975e39cc7cf8a61cc3ba76c81c64a3414f38d604ca1bf9f4647c29cd92d5b362eff15cf7bb1e3a52df798a52aafac2f09420a68af9686e2c1a294ccf426b5aac64899486011fc7eca8e79b8"
    return encSrcKey


def N_comment(id,ReviewCount):
    ReviewKeep = 0
    KeepFile = os.getcwd() + os.sep + "Review" + os.sep + str(id) + ".nie"
    fp = open(KeepFile, 'w')
    PageNum = ReviewCount/100
    Count = 100
    if ReviewCount%100 != 0:
        PageNum +=1
    for RP in xrange(1,PageNum+1):
        if RP == PageNum:
            Count = ReviewCount%100
        data = {
        'params':Nie_get_params(RP,Count),
        'encSecKey':Nie_get_encSecKey()
        }
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Cookie': 'JSESSIONID-WYYY=vDeNaw5OspW8kcNaX%5CsngVIwR3Z%2FigZ0HHGIb2duQgPm%2FFhGpQs6c26bKN3xf9tOatRbKk1JlTpJCiNsrZCsACk%2BN296WbpNc%2Fn96i8Ih6NYvHkjqXRR165SZAxv9YkkSAzfH9WTgCnyJUV6PEB9mm%2BJsduyy0B%5Cf2S7zXIdbls2hHY7%3A1519467798967; _iuqxldmzr_=32; _ntes_nnid=fc7bf97086aab1c7e5ea7559945fc3fe,1519465998987; _ntes_nuid=fc7bf97086aab1c7e5ea7559945fc3fe; __utma=94650624.1089055467.1519466000.1519466000.1519466000.1; __utmz=94650624.1519466000.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ngd_tid=izuEtMCQO5AHgNjd7VBI%2FItSs427hfCz',
        }
        url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_" + str(id) + "?csrf_token="
        r1 = rs.post(url,headers = headers,data = data).content
        json_1 = json.loads(r1)
        if "hotComments" in json_1:
            fp.write("最热评论:"+'\r\n')
            print u"最热评论"+ str(len(json_1["hotComments"]))
            for i in xrange(0,len(json_1["hotComments"])-1):
                HotReview = json_1["hotComments"][i]['user']['nickname'] + " : " + json_1["hotComments"][i]['content'] + " (" + str(json_1["hotComments"][i]['likedCount']) + ") "+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(str(json_1['hotComments'][i]['time'])[0:10])))
                print HotReview
                fp.write(HotReview.encode('utf-8')+'\r\n')
                print
            fp.write("最新评论:"+'\r\n')
        print
        print u"最新评论" + str(len(json_1['comments']))
        ReviewKeep+=len(json_1['comments'])
        for i in xrange(0,len(json_1['comments'])):
            NewReview = json_1['comments'][i]['user']['nickname'] + " : " + json_1['comments'][i]['content'] + " (" + str(json_1["comments"][i]['likedCount']) + ") "+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(float(str(json_1['comments'][i]['time'])[0:10])))
            print NewReview
            fp.write(NewReview.encode('utf-8')+'\r\n')
            print
    fp.close()
    print str(ReviewKeep)+u" 条评论已经保存在 "+ KeepFile

if __name__=='__main__':
    N_comment(id=418603077,ReviewCount = 10)  #id为歌曲的id ReviewCount为最新的多少条评论