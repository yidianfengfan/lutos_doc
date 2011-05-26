'''
Created on 2011-5-26

@author: leishouguo
'''
from django.conf.locale import cs
import datetime
import signal
import threading
import time


# 任务信号处理
_DATA_EVENT_ = threading.Event()
_DATA_EVENT_.set()
def dataSignalHandler(signum, frame): 
    _DATA_EVENT_.set()
signal.signal(signal.SIGUSR1, dataSignalHandler)
 
# 程序终止信号处理
_END_EVENT_ = threading.Event()
_END_EVENT_.clear()
def endSignalHandler(signum, frame):
    _END_EVENT_.set()
    _DATA_EVENT_.set()
signal.signal(signal.SIGTERM, endSignalHandler)
 
############################################################
 
_SLOCK_ = threading.Lock() #更新任务队列锁
 
class Server: 
 
    def __init__(self, num, cktime):
        self.max = (datetime.datetime(2000,1,1), '') #队列中最大时间、对应流水号
        self.num = num
        self.sendQueue = {} #待发送短信队列
 
    def run(self):
        '''主控线程'''
        svc = [
            threading.Thread(target = self.doReceive),
            threading.Thread(target = self.doTask),
        ]
        for i in svc:
            i.start()
        while not _END_EVENT_.isSet():
            _END_EVENT_.wait(60)
        for i in svc:
            i.join()
 
    def doReceive(self):
        '''可变时更新内存队列'''
        minsec = 12
        while not _END_EVENT_.isSet():
            _DATA_EVENT_.wait(minsec) #多线程?
 
            minsec = self.updateCkQueue()
            if minsec > 0: #如果没有需要及时处理信息
                _DATA_EVENT_.clear()
 
    def updateCkQueue(self):
        '''更新队列，返回下一个记录最短时间'''
        ids = self.sendQueue.keys() 
        #从数据库获取任务
        #多取一条是为了获得下次查询数据库的最短时间
        rows = cs.getRecords(ids, self.num+1) 
        if not rows:
            return 12
 
        minsec = '' #最短多少秒取
        for row in rows:
 
            if len(self.sendQueue) < self.num: #队列未满，直接入队
                self.sqin(row['m_id'], row)
                if row['m_dotime'] > self.max[0]:
                    self.modifyMax((row['m_dotime'], row['m_id']))
                continue
 
            if row['m_dotime'] < self.max[0]:#当前记录更急
                d = self.sqout(self.max[1])
                self.sqin(row['m_id'], row) #入库
                self.modifyMax((row['m_dotime'], row['m_id']))
                self.modifyMax('')
                row = d #出狱后的记录
 
            mt = row['m_dotime'] - time.time()
            minsec = minsec == '' and mt #初始化minsec
            minsec = min(mt, minsec)
 
        return minsec !='' and minsec or 0
 
    def doTask(self):
        '''检查内存队列'''
        while not _END_EVENT_.isSet():
            for i in self.sendQueue.keys():
                d = self.sendQueue[i]
                if datetime.datetime.now() > d['m_dotime']: #该处理了
            _END_EVENT_.wait(1)
 
 
    def modifyMax(self, data = ''):
        '''修改当前最大时间和序列号'''
        if data:
            self.max = data
            return data
 
        for i in self.sendQueue.keys(): #重新获取最大时间
            d = self.sendQueue[i]
            self.max = d['m_dotime'] > self.max[0] and (d['m_dotime'], i) or self.max
 
 
    @ThreadUtil.lockingCall(_SLOCK_)
    def sqin(self, id, data):
        self.sendQueue[id] = data
 
    @ThreadUtil.lockingCall(_SLOCK_)
    def sqout(self, id):
        return self.sendQueue.pop(id)