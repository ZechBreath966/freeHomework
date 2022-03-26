#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time : 19:31
# @Author : 赵锦瑞
# @File : profile1.py
# @Software : PyCharm
from pypinyin import pinyin, Style

"""
思路：
由图片识别文字再把文字粘贴在一个文本文件上，
用pinyin库来实现按个汉字的拼音拼法，
将拼音的元辅音对应一张双拼的音节表，
替换拼音为双拼打字的音节表。
"""


# 读取文件获得字串大列表
def getInfo(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        return f.readlines()


# 去除getInfo()获得的列表中每个字串的换行符
def removeLine(targetList):
    for i in range(len(targetList)):
        targetList[i] = targetList[i].replace("\n", "")
    return targetList


# 将removeLine()所获得的处理后列表中的每个汉字转化为拼音
def charList2Pinyin(charList):
    for i in range(len(charList)):
        charList[i] = pinyin(charList[i], Style(0))
    return charList


# 将charList2Pinyin()获得的列表去除list
def iWantChar(charList):
    li = []
    for i in charList:
        for j in i:
            li.extend(j)
    return li


# targetList = iWantChar(charList2Pinyin(removeLine(getInfo("1.txt"))))
# print(targetList)
# print(len(targetList))


def baiLan(targetList):
    li = []
    for i in range(len(targetList)):
        if len(targetList[i]) == 1:
            li.append(targetList[i])
        elif targetList[i] == 'ang':
            li.append('oa')
        else:
            if targetList[i][0:2] == 'sh':
                temp = "u"
                targetList[i] = temp + targetList[i][2:]
            elif targetList[i][0:2] == 'ch':
                temp = 'i'
                targetList[i] = temp + targetList[i][2:]
            elif targetList[i][0:2] == 'zh':
                temp = 'v'
                targetList[i] = temp + targetList[i][2:]

            if targetList[i][1:] == 'iu':
                temp = 'q'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'ia' or targetList[i][1:] == 'ua':
                temp = 'w'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'e':
                temp = 'e'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'uan' or targetList[i][1:] == 'er':
                temp = 'r'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'ue':
                temp = 't'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'ü' or targetList[i][1:] == 'uai':
                temp = 'y'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'u':
                temp = 'u'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'i':
                temp = 'i'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'o' or targetList[i][1:] == 'uo':
                temp = 'o'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'un':
                temp = 'p'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'a':
                temp = 'a'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'ong' or targetList[i][1:] == 'iong':
                temp = 's'
                li.append(targetList[i][0] + temp)
            elif targetList[i][1:] == 'iang' or targetList[i][1:] == 'uang':
                temp = 'd'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'en':
                temp = 'f'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'eng':
                temp = 'g'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'ang':
                temp = 'h'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'an':
                temp = 'j'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'ao':
                temp = 'k'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'ai':
                temp = 'l'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'ing':
                temp = ';'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'ei':
                temp = 'z'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'ie':
                temp = 'x'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'iao':
                temp = 'c'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'ui' or targetList[i][1:] == 'ue':
                temp = 'v'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'ou':
                temp = 'b'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'in':
                temp = 'n'
                li.append(targetList[i][0] + temp)

            elif targetList[i][1:] == 'ian':
                temp = 'm'
                li.append(targetList[i][0] + temp)
            else:
                li.append(targetList[i])
    return li


# print(len(baiLan(targetList)))
def startBaiLan(fileName):
    targetList = iWantChar(charList2Pinyin(removeLine(getInfo(fileName))))
    print(baiLan(targetList))
while True:
    if input() == 'q':
        break
    else:
        filename = input("请输入要摆烂的文件：")
        startBaiLan(filename)