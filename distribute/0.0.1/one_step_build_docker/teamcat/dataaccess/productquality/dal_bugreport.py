#coding=utf-8
'''
Created on 2015-2-28

@author: Devuser
'''

from doraemon.productquality.models import BugFreeMapping
import mysql.connector

class DAL_BugReport(object):
    '''
    data access for bug report
    '''
    opend_bugcounts_perday_sql=r"select LEFT(t2.ActionDate,10) as BugDate,count(*) as BugCounts  from bf_BugInfo t1"+\
                                r" inner join  bf_TestAction t2 on t1.BugID=t2.IdValue where t2.ActionDate>='{STARTDATE}' and t2.ActionDate<='{ENDDATE}' "+\
                                r" and t2.ActionType in ('Opened','Activated') and ModuleID={MODULEID} group by t1.ModulePath,BugDate"
    
    resolved_bugcounts_perday_sql=r"select LEFT(t2.ActionDate,10) as BugDate,count(*) as BugCounts  from bf_BugInfo t1"+\
                                r" inner join  bf_TestAction t2 on t1.BugID=t2.IdValue where t2.ActionDate>='{STARTDATE}' and t2.ActionDate<='{ENDDATE}' "+\
                                r" and t2.ActionType='Resolved' and ModuleID={MODULEID} group by t1.ModulePath,BugDate"
    
    closed_bugcounts_perday_sql=r"select LEFT(t2.ActionDate,10) as BugDate,count(*) as BugCounts  from bf_BugInfo t1"+\
                                r" inner join  bf_TestAction t2 on t1.BugID=t2.IdValue where t2.ActionDate>='{STARTDATE}' and t2.ActionDate<='{ENDDATE}' "+\
                                r" and t2.ActionType='Closed' and ModuleID={MODULEID} group by t1.ModulePath,BugDate"
    opend_bugcounts_all_sql=r"select count(*) as BugCounts  from bf_BugInfo t1"+\
                                r" inner join  bf_TestAction t2 on t1.BugID=t2.IdValue where t2.ActionDate>='{STARTDATE}' and t2.ActionDate<='{ENDDATE}' "+\
                                r" and t2.ActionType in ('Opened','Activated') and ModuleID={MODULEID} "
    
    @staticmethod
    def get_bugcounts(sqltext,startdate,enddate,moudleid):
        resultlist=list()
        cnx =DAL_BugReport.get_bugfree_connection()
        cursor = cnx.cursor()
        query =DAL_BugReport.get_bugcounts_query(sqltext,startdate, enddate, moudleid)
        cursor.execute(query)
        for item in cursor:
            resultlist.append(item)
        cnx.close()
        return resultlist
            
    @staticmethod
    def get_opened_bugcounts_perday(startdate,enddate,moudleid):
        return DAL_BugReport.get_bugcounts(DAL_BugReport.opend_bugcounts_perday_sql, startdate, enddate, moudleid)
    
    @staticmethod
    def get_resolved_bugcounts_perday(startdate,enddate,moudleid):
        return DAL_BugReport.get_bugcounts(DAL_BugReport.resolved_bugcounts_perday_sql, startdate, enddate, moudleid)
    
    @staticmethod
    def get_closed_bugcounts_perday(startdate,enddate,moudleid):
        return DAL_BugReport.get_bugcounts(DAL_BugReport.closed_bugcounts_perday_sql, startdate, enddate, moudleid)
    
    @staticmethod
    def get_opened_bugcounts_all(startdate,enddate,moudleid):
        return DAL_BugReport.get_bugcounts(DAL_BugReport.opend_bugcounts_all_sql,startdate, enddate, moudleid)
    
    @staticmethod
    def get_bugfree_module(doraemonprojectid,platformid):
        items=BugFreeMapping.objects.all().filter(DoraemonProjectID=doraemonprojectid).filter(DoraemonPlatformID=platformid)
        if len(items):
            return items[0]
        else:
            return None
    
    @staticmethod
    def get_bugfree_connection():
        return mysql.connector.connect(user='root',password='zhu88jie',host='10.3.254.21',port='3306', database='bugfree')
    
    @staticmethod
    def get_bugcounts_query(sourcesql,startdate,enddate,moudleid):
        query =sourcesql.replace('{STARTDATE}',startdate)
        query =query.replace('{ENDDATE}',enddate)
        query=query.replace('{MODULEID}',str(moudleid))
        return query
        
        
        
    
    
    
        