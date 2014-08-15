import glob, os
import config as cfg
from datetime import datetime



class postProcessor(object):
    def __init__(self):
        self.ls = []
        for f in glob.glob(cfg.results_fp+'\\csv\\*.csv'):
            self.ls.append(datetime.strptime(os.path.basename(f)[:-4], '%d-%m-%Y'))
    def exportEveryNthDay(self,n,start = 0, end = 1000000000):
        if start != 0:
            start = self.indexDate(start)
        if end != 1000000000:
            end = self.indexDate(end)
        self.ls = self.ls[start:end:n]
        self.exportData()
    def exportData(self):
        print self.ls
        print 'done'
    def indexDate(self,datestring):
        tv = datetime.strptime(datestring, '%d-%m-%Y')
        try:
            return self.ls.index(tv)
        except:
            return 0  # Add check here to see if date is out of range - too high or too low.

a = postProcessor()
a.exportEveryNthDay(10,start = '05-01-2013',end = '20-01-2013')