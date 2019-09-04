# 数据库配置
HOSTNAME = '127.0.0.1'
DATABASE = 'access_code'
USERNAME = 'root'
PASSWORD = 'yhchdev666'

DB_URI = 'mysql://{}:{}@{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, DATABASE
)