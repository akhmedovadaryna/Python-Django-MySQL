import MySQLdb as mdb
import MySQLdb as mdb1
import sys
from xml.dom.minidom import *
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree as et

class DB_1(object):

    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is not None:
            return
        try:
            self.connection = mdb.connect('127.0.0.1', 'root', '12345', 'mdb1')

        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            self.connection = None

    def close(self):
        if self.connection is not None:
            self.connection.close()
        self.connection = None

    def get_file_list(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("select idFile,name_f,size,type,name_u,year,B_day,idstorage,name,date_s_add,date_s_change from File left join user on File.user_name_u=user.name_u left join Cloud_storage on  File.Cloud_storage_idstorage=Cloud_storage.idstorage")
        self.close()
        return cur.fetchall()

    def diapason(self, first, last):
        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("select idFile,name_f,size,type,name_u,year,B_day,idstorage,name,date_s_add,date_s_change from File left join user on File.user_name_u=user.name_u left join Cloud_storage on  File.Cloud_storage_idstorage=Cloud_storage.idstorage WHERE year>'%s' and year<'%s'" % (first,last,))
        self.close()
        return cur.fetchall()
    def diapason_1(self, first, last):
        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("select idFile,name_f,size,type,name_u,year,B_day,idstorage,name,date_s_add,date_s_change from File left join user on File.user_name_u=user.name_u left join Cloud_storage on  File.Cloud_storage_idstorage=Cloud_storage.idstorage WHERE idstorage>'%s' and idstorage<'%s'" % (first,last,))
        self.close()
        return cur.fetchall()
    def save_file(self, name_f, size, type, user_name_u, Cloud_storage_idstorage):
        self.connect()

        cur = self.connection.cursor()

        cur.execute("INSERT INTO File (name_f, size, type, user_name_u, Cloud_storage_idstorage ) VALUES('%s', '%s','%s','%s','%s')" %
                    (name_f, size, type, user_name_u, Cloud_storage_idstorage,))
        cur.execute("commit")
        self.close()

    def get_Cloud_storage_list(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb1.cursors.DictCursor)
        cur.execute("select * from Cloud_storage")
        self.close()
        return cur.fetchall()

    def save_cloud(self, name,date_s_add,date_s_change):
        self.connect()

        cur = self.connection.cursor()

        cur.execute("INSERT INTO Cloud_storage (name,  date_s_add,   date_s_change ) VALUES('%s', '%s','%s')" %
                    (name,  date_s_add,   date_s_change,))
        cur.execute("commit")
        self.close()

    def get_user_list(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("SELECT * FROM user")
        self.close()
        return cur.fetchall()

    def save_user(self, name_u, B_day, year):
        self.connect()

        cur = self.connection.cursor()

        cur.execute("INSERT INTO user (name_u, B_day, year ) VALUES('%s', '%s', '%s')" %
                    (name_u,B_day,year))
        cur.execute("commit")
        self.close()

    def change_user(self, name_u, B_day, year, key):
        self.connect()

        cur = self.connection.cursor()
        if name_u != '':
         cur.execute("UPDATE user SET name_u='%s' WHERE name_u='%s'" %
                    (name_u,key,))
        if B_day != '':
         cur.execute("UPDATE user SET B_day='%s' WHERE name_u='%s'" %
                    (B_day,key,))
        if year != '':
          cur.execute("UPDATE user SET year='%s' WHERE name_u='%s'" %
                    (year,key,))
        cur.execute("commit")
        self.close()

    def load(self):

        XML_file = '/home/darina/d_b/bin/D_B_second/student/files/1.xml'
        l = []
        i = 0
        for el in et.parse(XML_file).getroot().findall(".//Cloud_storage/name"):
            l.append({})
            l[i]['name'] = el.text
            i = i+1

        i=0
        for el in et.parse(XML_file).getroot().findall(".//Cloud_storage/date_s_add"):
            l[i]['date_s_add'] = el.text
            i = i+1

        i=0
        for el in et.parse(XML_file).getroot().findall(".//Cloud_storage/date_s_change"):
            l[i]['date_s_change'] = el.text
            i = i+1



        u = []
        i = 0
        for el in et.parse(XML_file).getroot().findall(".//user/name_u"):
            u.append({})
            u[i]['name_u'] = el.text
            i = i+1

        i=0
        for el in et.parse(XML_file).getroot().findall(".//user/B_day"):
            u[i]['B_day'] = el.text
            i = i+1

        i=0
        for el in et.parse(XML_file).getroot().findall(".//user/year"):
            u[i]['year'] = el.text
            i = i+1

        self.connect()

        cur = self.connection.cursor()

        cur.execute("DELETE FROM user")
        cur.execute("DELETE FROM Cloud_storage")
        for i in l:
         cur.execute("INSERT INTO Cloud_storage (name, date_s_add, date_s_change) VALUES('%s', '%s', '%s')" %
                    (i['name'], i['date_s_add'], i['date_s_change'],))

        for i in u:
         cur.execute("INSERT INTO user (name_u, B_day, year) VALUES('%s', '%s', '%s')" %
                    (i['name_u'],i['B_day'],i['year'],))

        cur.execute("commit")
        self.close()

    def change_file(self, name_f, size, type, user_name_u, Cloud_storage_idstorage, key):
        self.connect()

        cur = self.connection.cursor()
        if name_f != '':
         cur.execute("UPDATE File SET name_f='%s' WHERE idFile='%s'" %
                    (name_f,key,))
        if size != '':
         cur.execute("UPDATE File SET size='%s' WHERE idFile='%s'" %
                    (size,key,))
        if type != '':
         cur.execute("UPDATE File SET type='%s' WHERE idFile='%s'" %
                    (type,key,))
        if user_name_u != '':
         cur.execute("UPDATE File SET user_name_u='%s' WHERE idFile='%s'" %
                    (user_name_u,key,))
        if Cloud_storage_idstorage != '':
         cur.execute("UPDATE File SET Cloud_storage_idstorage='%s' WHERE idFile='%s'" %
                    (Cloud_storage_idstorage,key,))
        cur.execute("commit")
        self.close()

    def delete(self,idFile):

        self.connect()

        cur = self.connection.cursor()

        cur.execute("DELETE FROM File WHERE idFile='%s'" % (idFile,))


        cur.execute("commit")
        self.close()

    def poisk_1(self,Poisk):


        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("select idFile,name_f,size,type,name_u,year,B_day,idstorage,name,date_s_add,date_s_change from File left join user on File.user_name_u=user.name_u left join Cloud_storage on  File.Cloud_storage_idstorage=Cloud_storage.idstorage WHERE name_u='%s'" % (Poisk,))
        self.close()
        return cur.fetchall()


    def poisk_2(self,Poisk_1):


        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("select idFile,name_f,size,type,name_u,year,B_day,idstorage,name,date_s_add,date_s_change from File left join user on File.user_name_u=user.name_u left join Cloud_storage on  File.Cloud_storage_idstorage=Cloud_storage.idstorage WHERE name='%s'" % (Poisk_1,))
        self.close()
        return cur.fetchall()


    def search_1(self,Search_1,Search_2):


        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        if Search_2 == '':
            cur.execute("select idFile,name_f,size,type,name_u,year,B_day,idstorage,name,date_s_add,date_s_change from File left join user on File.user_name_u=user.name_u left join Cloud_storage on  File.Cloud_storage_idstorage=Cloud_storage.idstorage WHERE MATCH (name_f) AGAINST('%s'IN BOOLEAN MODE)" % (Search_1,))
        else:
            cur.execute("select idFile,name_f,size,type,name_u,year,B_day,idstorage,name,date_s_add,date_s_change from File left join user on File.user_name_u=user.name_u left join Cloud_storage on  File.Cloud_storage_idstorage=Cloud_storage.idstorage WHERE MATCH (name_f) AGAINST('%s -%s'IN BOOLEAN MODE)" % (Search_1,Search_2,))
        self.close()
        return cur.fetchall()
