# encoding:utf-8

import redis
import sys
import datetime
import time
parseFile = '/opt/home/logs/sns.u.soa-ice.log'
timestamp = 0
#Python格式化日期时间的函数为datetime.datetime.strftime()；由字符串转为日期型的函数为：datetime.datetime.strptime()

import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

if __name__ == '__main__':
    print 'start parse stats...'
    print 'args==>' , sys.argv
    
    #parseFile = sys.argv[1]
    with open(parseFile, "r") as f:
        line = f.readline()
        while line != "":
            # Do stuff with byte.
            if(line.find("log stat") > 0):
                # print datetime.datetime.strptime(line[0:19], "%Y-%m-%d %H:%M:%S" )
                timestamp =  time.mktime(time.strptime(line[0:19], "%Y-%m-%d %H:%M:%S" ) )
                
                
            if line.find('@') > 0 and line.find("#") > 0:
                for op in line.split("@"):
                    if(op.strip() != ""):
                        statsEntry = op.split("#")
                        if(len(statsEntry) == 4):
                            #app =  app[20:] if app.find("StatUtil") > 0 else app
                            key = "%s_%s_%s"%(statsEntry[0], statsEntry[1],timestamp)
                            value = "%s_%s" %(statsEntry[2], statsEntry[3])
                            print key, "==>" , value
                            r.set( key, value)
                
            line = f.readline()
        r.connection_pool.disconnect()