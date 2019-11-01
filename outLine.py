#!/usr/bin/env python
# coding=utf-8


import datetime
import copy
import urllib
import os
import socket


socket.setdefaulttimeout(300)
appdict = {}
userdict = {}
logs = []


def getlogs():
    """Fetches rows from a file
              Args:
              Returns:
                    nothing is return
              """
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    hour = datetime.datetime.strptime(str(yesterday) + "-00", '%Y-%m-%d-%H')
    logs.append(hour.strftime("%Y-%m-%d-%H") + ".log")
    for i in range(0, 23):
        hour = hour + datetime.timedelta(hours=1)
        i = i + 1
        logs.append(hour.strftime("%Y-%m-%d-%H") + ".log")
    return


def getdatafromfile(file, dict):
    """Fetches rows from a file
              Args:
                  file: log file
                  dict: A sequence of strings representing the key of each table row
                      to fetch.
              Returns:
                    nothing is return
              """
    for line in open(file, 'r').readlines():
        tmp = line.split('\n')
        data = tmp[0].split('\t')
        if data != ['']:
            dict[data[1]] = data
    return


def computeAppdatafromfile(file, dict):
    """Fetches rows from a file
              Args:
                  file: log file
                  dict: A sequence of strings representing the key of each table row
                      to fetch.
              Returns:
                    nothing is return
              """
    for line in open(file, 'r').readlines():
        tmp = line.split('\n')
        data = tmp[0].split('\t')
        if data != ['']:
            if dict.get(data[1]):
                for i in range(2, len(data)):
                    dict.get(data[1])[i] = int(dict.get(data[1])[i]) + int(data[i])
                    i + 1
            else:
                dict[data[1]] = data
    return dict












getlogs()

##统计24个日志文件。
for i in range(0, 24):
    urllib.urlretrieve(
        "http://10.187.44.25:8200/rest/io/download/from/ceph"
        "?bucket=asr-count&sourceFile=" + logs[i],
        logs[i])
    # print logs[i]
    computeAppdatafromfile(logs[i], appdict)


##删除24个日志文件。
for i in range(0, 24):
    os.remove(logs[i])
