import sys,os,configparser
# 将当前目录加入模块搜索路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 将项目根目录加入模块搜索路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 设置环境变量
os.environ['PROJECT_PATH'] = os.path.dirname(os.path.abspath(__file__))

from lib.api import app

#创建配置文件对象
con = configparser.ConfigParser()

#读取配置文件
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'config.ini')
con.read(config_path, encoding='UTF-8')


#获取配置文件中的host和port配置，如果提示 “以一种访问权限不允许的方式做了一个访问套接字的尝试” 那么可能因为是端口被占用了
host = con.get('global','host')
port = con.get('global', 'port')

if __name__ == '__main__':
    app.run(
        host=host,
        port=port,
    )

#如果作为web项目启动可以使用以下命令在终端中运行
#gunicorn FLASK-PROJECT:app -w 6 -b 0.0.0.0:8080