import os,configparser,pymysql,redis


#创建配置文件对象
con = configparser.ConfigParser()

#读取配置文件
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.ini')
con.read(config_path, encoding='UTF-8')

#获取mysql连接信息
Mysql_DBName = con.get('mysql', 'DBName')
Mysql_Host = con.get('mysql', 'Host')
Mysql_User = con.get('mysql', 'User')
Mysql_Pass = con.get('mysql', 'Pass')
Mysql_Port = con.get('mysql', 'Port')

#获取redis连接信息
Redis_Host = con.get('redis', 'Host')
Redis_Port = con.get('redis', 'Port')
Redis_DB_Num = con.get('redis', 'DB')

#mysql数据库方法
def Mysql_DB(sql):
    mysql_con = pymysql.connect(Mysql_Host, Mysql_User, Mysql_Pass, Mysql_DBName, Mysql_Port)
    cur = mysql_con.cursor()
    cur.execute(sql)
    if sql.strip()[:6].upper()=='SELECT':
        res = cur.fetchall()
    else:
        cur.commit()
        res = 'Commit OK'
    cur.close()
    mysql_con.close()
    return res

#redis数据库方法
def Redis_DB(Redis_key, Redis_value=None,Key_Expire_Time=None):
    Redis_con = redis.Redis(Redis_Host, Redis_Port, Redis_DB_Num)
    if Redis_con:
        Redis_con.set(Redis_key, Redis_value, Key_Expire_Time)
        res = 'Redis key set OK'
    else:
        res = Redis_con.get(Redis_key).decode()
    return res