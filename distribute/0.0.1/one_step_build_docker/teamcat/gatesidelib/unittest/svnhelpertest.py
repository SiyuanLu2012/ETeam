#coding=utf-8
#coding=utf-8
'''
Created on 2014-12-10

@author: Devuser
'''
import unittest
import time
from gatesidelib.svnhelper import SvnHelper
import datetime
import os


class SvnHelperTest(unittest.TestCase):


#     def test_get_allcodelines(self):
#         svn_helper=SvnHelper('https://svn.sys.com/user.hu.com/branches/sdk3.7','autotest','Nopass.2')
#         print(svn_helper.get_allcodelines('7966'))
#     
#     def test_get_newcodelines(self):
#         svn_helper=SvnHelper('https://svn.sys.com/branches/sdk3.7','autotest','Nopass.2')
#         print(svn_helper.get_newcode_lines('7000','7966'))
#         
#     def test_get_deletecodelines(self):
#         svn_helper=SvnHelper('https://svn.sys.com/branches/sdk3.7','autotest','Nopass.2')
#         print(svn_helper.get_deletecode_lines('7000','7966'))
#     
#     def test_get_commit_log(self):
#         svn_helper=SvnHelper('https://svn.sys.com/branches/sdk3.7','autotest','Nopass.2','d:\\gateside.log')
#         print(svn_helper.get_commitlog(str(int("1991")+1),"1991")[1].decode('gb2312'))
#       
#     def testNumber(self):
#         print("15.8".isdigit())
#     def testreadfile(self):
#         file=open(r"d:\\gateside.log",'r')
#         linelist=list()
#         for line in file:
#             linelist.append(line)
#         linelist.reverse()
#         for line in linelist:
#             print(line.decode('gb2312'))
    def testwe(self):
        d='2013-03-29 15:07:34'
        now=time.strptime(d,'%Y-%m-%d %H:%M:%S')
        start=datetime.date(now.tm_year,now.tm_mon,now.tm_mday)
        print((datetime.date.today()-start).days)

#         os.system('cd "e:\\dushubus" & git pull --username autotest --password Nopass.2 >> git5.log')
        
#     def test2(self):
#         svn_helper=SvnHelper('https://svn.sys.com/branches/sdk3.7','autotest','Nopass.2','d:\\gateside.log')
#         print(svn_helper.get_linecounts("E:\\CommitLog\\Svn\\BigFoot1419229934.71.log",'+'))
        
            
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()