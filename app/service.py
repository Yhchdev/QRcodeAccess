from model import queryObject
import requests

# 获取硬件上传的解析后的字符 然后与数据库的值做匹配
def prossMsg(mes):
    splitList  = str(mes).split("'")
    idCardSha256  = splitList[1]
    accessObj = queryObject(idCardSha256)
    # 能查出记录 =>记录有合法记录  返回right
    if(accessObj!=None):
        requests.get('http://127.0.0.1:5000/mqtt/pub/right')
    else:
        requests.get('http://127.0.0.1:5000/mqtt/pub/error')



