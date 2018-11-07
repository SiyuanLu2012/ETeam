#coding=utf-8
'''
Created on 2014-11-27

@author: Devuser
'''
import unittest
from gatesidelib.common.simplelogger import SimpleLogger


class Test(unittest.TestCase):


    def testName(self):
        SimpleLogger.logger.error("fsdfsadfsdafsadfsadfdsa");
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    testCase=Test()
    testCase.testName()