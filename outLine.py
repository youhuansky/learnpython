#!/usr/bin/env python
# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.sql import text
import datetime
import copy
import urllib
import os
import socket


url = "mysql+pymysql://id_operation:3WskV4bUxIM9G@smartbns.aipcustomer-bmi0000.xdb.all.serv:5094/id_operation"
engine = create_engine(url, echo=True)
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


def computeUserDatefromDict(appdict, userdict):
    """Fetches rows from a file
              Args:
                  appdict: appdict store app info
                  userdict: userdict store user info
              Returns:
                    nothing is return
              """
    for appid in appdict.keys():
        userId = getUserId(appid)
        if userId != []:
            isexcess = 0
            excess_time = 0
            temp = getNum(userId)
            if temp[0][0] is not None:
                num = temp[0][0]*3600
                if num < (int(appdict.get(appid)[10]) + int(appdict.get(appid)[11])):
                    isexcess = 1
                    excess_time = (int(appdict.get(appid)[10]) + int(appdict.get(appid)[11])) - num

            appdict.get(appid).append(isexcess) 
            appdict.get(appid).append(excess_time)  

            if userdict.get(userId[0][1]):
                for i in range(2, len(userdict.get(userId[0][1]))):
                    a = int(userdict.get(userId[0][1])[i]) + int(appdict.get(appid)[i])
                    userdict.get(userId[0][1])[i] = a
            else:
                userdict[userId[0][1]] = copy.deepcopy(appdict.get(appid))
    return userdict


def getUserId(appId):
    """Fetches rows from a file
                     Args:
                         appId: get cloud_uid from database.
                     Returns:
                         return bdc_user_id and cloud_id
                     """
    with engine.connect() as con:
        rs = con.execute('SELECT bdc_user_id,cloud_uid from tb_operation_app where bdc_app_id=' + appId)
        userId = rs.fetchall()
        return userId


def getNum(userId):
    """Fetches rows from a file
                          Args:
                              userId: get order num from database.
                          Returns:
                              return num
                          """
    if userId != []:
        bdc_user_id = userId[0][0]
        with engine.connect() as con:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            rs = con.execute(
                'select SUM(num) as num from tb_account_order where status =1 and conf_type=20001 and et >="' + nowTime + '" and account_id = ' + str(
                    bdc_user_id))
            num = rs.fetchall()

            return num


def insertAppRecord(record, userId):
    """Fetches rows from a file
                              Args:
                                  record: app info record
                                  dateconcurrency: the num of date concurrency
                              Returns:
                                  return nothing
                              """
    with engine.connect() as con:
        if userId != []:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            rs = con.execute(text(
                'INSERT INTO tb_offlineasr_app_record (bdc_app_id,date,upload_illegal_cnt,'
                'upload_single_cnt,upload_dual_cnt,upload_single_time,upload_dual_time,'
                'ar_single_cnt,ar_dual_cnt,ar_error_cnt,ar_single_time,ar_dual_time,'
                'cloud_uid,bdc_user_id,create_time,update_time,isexcess,excess_time)'
                ' VALUES (:bdc_app_id,:date,:upload_illegal_cnt,:upload_single_cnt,'
                ':upload_dual_cnt,:upload_single_time,:upload_dual_time,'
                ':ar_single_cnt,:ar_dual_cnt,:ar_error_cnt,:ar_single_time,:ar_dual_time,'
                ':cloud_uid,:bdc_user_id,:create_time,:update_time,:isexcess,:excess_time)'),
                bdc_app_id=record[1], date=record[0], upload_illegal_cnt=record[2],
                upload_single_cnt=record[3], upload_dual_cnt=record[4],
                upload_single_time=record[5],
                upload_dual_time=record[6], ar_single_cnt=record[7], ar_dual_cnt=record[8],
                ar_error_cnt=record[9], ar_single_time=record[10], ar_dual_time=record[11],
                cloud_uid=userId[0][1], bdc_user_id=userId[0][0],
                create_time=nowTime, update_time=nowTime,
                isexcess=record[12], excess_time=record[13])
        con.close()
        return


def insertUserRecord(record, userId):
    """Fetches rows from a file
                                 Args:
                                     record: user info record
                                     dateconcurrency: the num of date concurrency
                                 Returns:
                                     return nothing
                                 """
    with engine.connect() as con:
        if userId != []:
            nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            rs = con.execute(text(
                'INSERT INTO tb_offlineasr_record (date,upload_illegal_cnt,upload_single_cnt,'
                'upload_dual_cnt,upload_single_time,upload_dual_time,'
                'ar_single_cnt,ar_dual_cnt,ar_error_cnt,ar_single_time,ar_dual_time,cloud_uid,'
                'bdc_user_id,create_time,update_time,isexcess,excess_time)'
                ' VALUES (:date,:upload_illegal_cnt,:upload_single_cnt,:upload_dual_cnt,'
                ':upload_single_time,:upload_dual_time,'
                ':ar_single_cnt,:ar_dual_cnt,:ar_error_cnt,:ar_single_time,:ar_dual_time,'
                ':cloud_uid,:bdc_user_id,:create_time,:update_time,:isexcess,:excess_time)'),
                date=record[0], upload_illegal_cnt=record[2],
                upload_single_cnt=record[3], upload_dual_cnt=record[4],
                upload_single_time=record[5],
                upload_dual_time=record[6], ar_single_cnt=record[7],
                ar_dual_cnt=record[8],
                ar_error_cnt=record[9], ar_single_time=record[10],
                ar_dual_time=record[11],
                cloud_uid=userId[0][1], bdc_user_id=userId[0][0],
                create_time=nowTime, update_time=nowTime,
                isexcess=record[12], excess_time=record[13])
        con.close()
        return


getlogs()

##统计24个日志文件。
for i in range(0, 24):
    urllib.urlretrieve(
        "http://10.187.44.25:8200/rest/io/download/from/ceph"
        "?bucket=asr-count&sourceFile=" + logs[i],
        logs[i])
    print logs[i]
    computeAppdatafromfile(logs[i], appdict)

##内存中计算user级别数据
computeUserDatefromDict(appdict, userdict)

##循环插入app级别统计数据
for appid in appdict.keys():
    userId = getUserId(appid)
    insertAppRecord(appdict.get(appid), userId)

##循环插入user级别统计数据
for userid in userdict.keys():
    userId = getUserId(userdict.get(userid)[1])
    insertUserRecord(userdict.get(userid), userId)

##删除24个日志文件。
for i in range(0, 24):
    os.remove(logs[i])
