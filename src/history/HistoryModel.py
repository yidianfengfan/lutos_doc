# encoding: utf-8
'''
Created on 2011-4-6

@author: leishouguo
'''
class HistoryModel:
    def __init__(self, chaodai,  nianHao, beginYear, beginMonth, endYear, endMonth): 
        self.chaodai = chaodai
        self.nianHao = nianHao
        self.beginYear = beginYear
        self.beginMonth = beginMonth
        self.endYear = endYear
        self.endMonth = endMonth
    
def obj2dict(obj):
    """
    summary:
    """
    memberlist = [m for m in dir(obj)]
    _dict = {}
    for m in memberlist:
        if m[0] != "_" and not callable(m):
            _dict[m] = getattr(obj,m)

    return _dict

if __name__ == '__main__':
    m = HistoryModel("清", "顺治", 1638, 1, 1651, 2)
    print m
    
    d = obj2dict(m)
    
    print d
